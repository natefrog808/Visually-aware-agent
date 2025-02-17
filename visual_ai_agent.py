import os
import base64
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import torch
from daydreamsai.core.v1 import Agent, createDreams, action, task, context, z
from util.omniparser import Omniparser

# OmniParser Configuration
class OmniParserConfig:
    som_model_path = "../../weights/icon_detect/model.pt"
    caption_model_name = "florence2"
    caption_model_path = "../../weights/icon_caption_florence"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    BOX_TRESHOLD = 0.05

class ParseRequest(BaseModel):
    base64_image: str

# OmniParser Server Setup
app = FastAPI()
omniparser = Omniparser(vars(OmniParserConfig))

@app.post("/parse/")
async def parse_image(parse_request: ParseRequest):
    dino_labled_img, parsed_content_list = omniparser.parse(parse_request.base64_image)
    return {"som_image_base64": dino_labled_img, "parsed_content_list": parsed_content_list}

# Helper function to encode images
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Daydreams Agent Configuration
def setup_visual_agent():
    agent = createDreams({
        "model": "your_model_here",  # Placeholder for LLM model
        "inputs": {
            "screen_capture": input({
                "schema": z.object({}),
                "async handler": lambda data, ctx, agent: agent.parse_and_analyze_screen(),
            })
        },
        "actions": [
            action({
                "name": "parse_and_analyze_screen",
                "schema": z.object({}),
                "async handler": parse_and_analyze_screen,
            })
        ],
        "contexts": {
            "screen_context": context({
                "type": "screen_context",
                "schema": z.object({}),
                "render": lambda memory, ctx: memory.get("screen_info", "No screen info available")
            }),
        },
    })
    return agent

# Task for parsing and analyzing screen
@task("agent:parse_and_analyze_screen")
async def parse_and_analyze_screen(params, ctx):
    from tools.screen_capture import get_screenshot
    
    screenshot, screenshot_path = get_screenshot()
    image_base64 = encode_image(screenshot_path)
    
    # Send image to OmniParser for parsing
    response = requests.post("http://localhost:8000/parse/", json={"base64_image": image_base64})
    parsed_data = response.json()
    
    # Store parsed data in context
    ctx.memory.set("screen_info", parsed_data['parsed_content_list'])
    
    # Analyze with Groq
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if groq_api_key:
        groq_client = Groq(api_key=groq_api_key)
        analysis_prompt = f"Analyze the following UI elements:\n{parsed_data['parsed_content_list']}"
        analysis = groq_client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[{"role": "user", "content": analysis_prompt}],
            temperature=0.6,
            max_completion_tokens=256
        ).choices[0].message.content
        ctx.memory.set("screen_analysis", analysis)
        return {"parsed_data": parsed_data, "analysis": analysis}
    return {"parsed_data": parsed_data}

# Main execution
if __name__ == "__main__":
    import uvicorn
    visual_agent = setup_visual_agent()
    uvicorn.run(app, host="0.0.0.0", port=8000)

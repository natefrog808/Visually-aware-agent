## Visually-aware-agent

# Visual AI Agent with Daydreams and O[mniParser
](https://x.com/i/grok?text=mniParser%0A)
# Overview
This project merges the Daydreams framework with OmniParser to create an AI agent that can understand and interact with graphical user interfaces (GUIs). It utilizes screen parsing capabilities to inform AI decision-making processes, enhancing interaction with digital environments.

# Features
Screen Parsing: OmniParser analyzes screenshots to identify and label UI elements.
AI Decision Making: The Daydreams agent uses this parsed visual data to make context-aware decisions.
Groq Integration: Incorporates Groq's language model for deeper analysis or planning based on visual input.
Real-time Interaction: Captures, parses, and acts on screens dynamically.

# Requirements
Python: Version 3.8 or higher.
Dependencies:
fastapi for creating the OmniParser server.
pydantic for data validation.
groq for language model interactions.
torch for model handling (assuming OmniParser uses PyTorch).
requests for HTTP interactions.

Install these via:
bash
pip install fastapi pydantic groq torch requests

# Setup
Environment Variables
GROQ_API_KEY: You must set this in your environment:
bash
export GROQ_API_KEY=your_api_key_here

# File Structure
Ensure the following structure:
visual_ai_agent.py - Contains the main script for both server and agent setup.
util/omniparser.py - OmniParser implementation.
tools/screen_capture.py - For capturing screenshots.
weights/ - Directory for model weights:
icon_detect/model.pt
icon_caption_florence/

# Configuration
OmniParser Weights: Verify weights are at the paths specified in the OmniParserConfig class or update accordingly.
Module Paths: Adjust import paths if util.omniparser or tools.screen_capture are not in the expected locations.

# Usage
Run the system with:

bash
python visual_ai_agent.py

This script:
Starts the OmniParser server on localhost:8000.
Initializes a Daydreams agent configured for visual interaction.

# How It Works
Screen Capture: Utilizes get_screenshot() to capture the current screen.
Image Parsing: Sends the image to the OmniParser server for analysis.
Data Storage: Stores parsed data in the agent's memory context.
Analysis: Uses Groq to analyze the parsed data for decision-making or action planning.
Action: Executes actions based on the analysis within Daydreams.

# Customization
Model Paths: Update paths in OmniParserConfig if needed.
Server URL: Change the URL in parse_and_analyze_screen if not using localhost:8000.
Agent Actions: Add or modify actions in the Daydreams agent based on specific requirements.

# Development
Error Handling: Implement error catching, especially for network operations and model loading.
Logging: Add detailed logging for tracking operations.
Security: Secure API key handling and consider server authentication.

# Testing
Unit Tests: Test individual functions like screen capture, parsing, and Groq integration.
Integration Tests: Ensure all components work together seamlessly.

License
[Insert license information here]

# Acknowledgements
Thanks to the developers of Daydreams, OmniParser, Groq, and all relevant open-source libraries.

# Contributing
just do it


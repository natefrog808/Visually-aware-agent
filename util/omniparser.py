# util/omniparser.py

import torch
import base64
import io
from typing import Dict, List, Any
from PIL import Image
import numpy as np
from torchvision import transforms
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from transformers import BlipForConditionalGeneration, BlipProcessor
import json

class Omniparser:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Initialize YOLO-like object detection model (using Faster R-CNN here for simplicity)
        self.som_model = fasterrcnn_resnet50_fpn(pretrained=True).to(device)
        self.som_model.eval()
        
        # Initialize a caption model (using BLIP for this example)
        self.caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
        self.caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        
        print('Omniparser initialized with Faster R-CNN and BLIP for captioning!')

    def parse(self, image_base64: str) -> Tuple[str, List[Dict]]:
        """
        Parses the given base64 encoded image to detect and caption UI elements.

        :param image_base64: Base64 encoded string of the image to parse.
        :return: Tuple containing the labeled image (as base64) and a list of parsed content.
        """
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        print('Image size:', image.size)
        
        # Image preprocessing for model input
        transform = transforms.Compose([
            transforms.ToTensor()
        ])
        image_tensor = transform(image).unsqueeze(0).to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
        
        # Object Detection
        with torch.no_grad():
            detections = self.som_model(image_tensor)
        
        # Process detections
        boxes = detections[0]['boxes'].cpu().numpy()
        scores = detections[0]['scores'].cpu().numpy()
        labels = detections[0]['labels'].cpu().numpy()
        
        # Filter by confidence threshold
        high_conf_idx = scores >= self.config.get('BOX_TRESHOLD', 0.5)
        boxes = boxes[high_conf_idx]
        labels = labels[high_conf_idx]
        
        # Draw bounding boxes
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        parsed_content_list = []
        
        for box, label in zip(boxes, labels):
            x1, y1, x2, y2 = box.astype(int)
            draw.rectangle([x1, y1, x2, y2], outline="red")
            
            # Caption the detected region
            cropped_image = image.crop((x1, y1, x2, y2))
            inputs = self.caption_processor(images=cropped_image, return_tensors="pt").to(self.caption_model.device)
            
            with torch.no_grad():
                out = self.caption_model.generate(**inputs)
            caption = self.caption_processor.decode(out[0], skip_special_tokens=True)
            
            parsed_content_list.append({
                "type": "ui_element",
                "label": str(label),  # Assuming label corresponds to some predefined UI elements
                "bbox": [x1, y1, x2, y2],
                "caption": caption
            })
            
            # Draw caption text
            draw.text((x1, y1 - 10), caption, fill="red", font=font)

        # Convert annotated image back to base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        labeled_image_base64 = base64.b64encode(buffered.getvalue()).decode('ascii')

        return labeled_image_base64, parsed_content_list

# Note:
# - This implementation uses Faster R-CNN for detection which isn't as fast or accurate for UI elements as YOLO might be but serves as a placeholder.
# - BLIP is used for captioning, which might not be optimal for UI elements; consider using models like Florence2 for better results.
# - Error handling, performance optimization, and proper resource management (like closing images) are omitted for brevity but should be included in production code.
# - The bounding box drawing is very basic; you might want to use a dedicated library for more professional results.

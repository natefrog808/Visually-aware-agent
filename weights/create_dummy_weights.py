# weights/create_dummy_weights.py

import os
import torch

def create_dummy_model(directory, filename):
    """
    Creates a dummy PyTorch model file in the specified directory.

    :param directory: The directory where the model file should be created.
    :param filename: The name of the model file.
    """
    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)

    # Create a dummy tensor (just for demonstration, not a real model)
    dummy_tensor = torch.randn(1, 3, 224, 224)  # Example tensor, adjust as needed

    # Save this tensor as a model file
    model_path = os.path.join(directory, filename)
    torch.save(dummy_tensor, model_path)
    print(f"Dummy model saved at: {model_path}")

if __name__ == "__main__":
    # Create dummy model for icon detection
    create_dummy_model("weights/icon_detect", "model.pt")

    # Create dummy model for icon captioning
    create_dummy_model("weights/icon_caption_florence", "model.safetensors")  # Note: using .safetensors instead of .pt for variety

# weights/icon_detect/create_dummy_model.py

import os
import torch

def create_dummy_model(filename="model.pt"):
    """
    Creates a dummy PyTorch model file for icon detection.

    :param filename: Name of the file to save the dummy model, defaults to "model.pt".
    """
    # Ensure the directory exists
    directory = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(directory, exist_ok=True)

    # Create a dummy tensor to mimic a model state_dict
    # This is just an example; a real model would have more complex structure
    dummy_conv_weight = torch.randn(64, 3, 7, 7)  # Example convolution layer weights
    dummy_linear_weight = torch.randn(1000, 64 * 7 * 7)  # Example fully connected layer weights
    
    dummy_model = {
        'conv1.weight': dummy_conv_weight,
        'fc.weight': dummy_linear_weight,
    }

    # Save this dummy model
    model_path = os.path.join(directory, filename)
    torch.save(dummy_model, model_path)
    print(f"Dummy model saved at: {model_path}")

if __name__ == "__main__":
    create_dummy_model()

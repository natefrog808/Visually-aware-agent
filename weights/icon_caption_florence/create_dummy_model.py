# weights/icon_caption_florence/create_dummy_model.py

import os
import torch
import safetensors.torch

def create_dummy_model(filename="model.safetensors"):
    """
    Creates a dummy safetensors model file for icon captioning.

    :param filename: Name of the file to save the dummy model, defaults to "model.safetensors".
    """
    # Ensure the directory exists
    directory = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(directory, exist_ok=True)

    # Create dummy tensor data
    # Here we simulate a model with some layers
    dummy_embedding = torch.randn(512, 300)  # Simulating an embedding layer
    dummy_lstm_weight = torch.randn(512, 512 * 4)  # Simulating LSTM weights
    dummy_linear_weight = torch.randn(512, 1000)  # Simulating a final layer for vocabulary output

    dummy_model = {
        'embedding.weight': dummy_embedding,
        'lstm.weight_ih_l0': dummy_lstm_weight,
        'final_layer.weight': dummy_linear_weight,
    }

    # Save the model in safetensors format
    model_path = os.path.join(directory, filename)
    safetensors.torch.save_file(dummy_model, model_path)
    print(f"Dummy model saved at: {model_path}")

if __name__ == "__main__":
    create_dummy_model()

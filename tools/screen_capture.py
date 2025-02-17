# tools/screen_capture.py

import os
import pyautogui
import time
from pathlib import Path
from PIL import Image

def get_screenshot() -> Tuple[Image.Image, str]:
    """
    Captures the current screen and saves it to a temporary file.

    :return: A tuple containing:
             - The PIL Image object of the screenshot
             - The file path where the screenshot is saved
    """
    # Create a directory for storing temporary screenshots if it doesn't exist
    output_dir = "./tmp/screenshots"
    os.makedirs(output_dir, exist_ok=True)

    # Generate a unique filename for the screenshot
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = os.path.join(output_dir, f"screenshot_{timestamp}.png")

    # Capture the screen
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot to the defined path
    screenshot.save(screenshot_path)
    
    # Return the PIL Image object along with the path
    return screenshot, screenshot_path

if __name__ == "__main__":
    # Example usage when running this script directly
    screenshot, path = get_screenshot()
    print(f"Screenshot saved at: {path}")
    screenshot.show()  # Opens the image if a viewer is set up on your system

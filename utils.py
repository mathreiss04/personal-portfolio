import base64
import os

def get_image_as_base64(image_path):
    """Convert an image to base64."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
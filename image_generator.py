import requests
import os
from PIL import Image
from io import BytesIO

API_KEY = "8ed6a19ef7f4177fdb79eec1dab85eee9a4e6342147688a44f7c695535e56f02"  # Replace with your Together AI key

from together import Together
import requests
import os
from datetime import datetime

class TogetherImageGenerator:
    def __init__(self, api_key):
        """
        Initialize the image generator with API key
        """
        self.client = Together(api_key=api_key)
    
    def generate_image(self, prompt, 
                      model="stabilityai/stable-diffusion-xl-base-1.0",
                      steps=4, 
                      width=1024, 
                      height=1024,
                      filename=None):
        """
        Generate and save an image from text prompt
        Args:
            prompt: Text prompt for image generation
            model: Model to use for generation
            steps: Number of inference steps
            width: Width of output image
            height: Height of output image
            filename: Name to save the image (optional)
        Returns:
            Path to saved image or None if failed
        """
        try:
            # Generate image using Together API
            response = self.client.images.generate(
                prompt=prompt,
                model=model,
                steps=steps,
                width=width,
                height=height
            )
            
            # Get image URL from response
            image_url = response.data[0].url
            
            # Create filename if not provided
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"generated_image_{timestamp}.png"
            
            # Download and save the image
            return self._download_image(image_url, filename)
            
        except Exception as e:
            print(f"Error generating image: {str(e)}")
            return None

    def _download_image(self, url, filename):
        """Download image from URL and save to file"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return os.path.abspath(filename)
            
        except Exception as e:
            print(f"Error downloading image: {str(e)}")
            return None



import pytesseract
from PIL import Image


class ImageTextCLassifier:
    def get_text(self, image):
        image = Image.open(image)
        extracted_text = pytesseract.image_to_string(image)
        return extracted_text

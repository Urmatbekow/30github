from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('path_to_your_image.jpg')

extracted_text = pytesseract.image_to_string(image)

print(extracted_text)
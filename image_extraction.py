from PIL import Image
import pytesseract
from pytesseract import Output
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('path_to_your_image.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

pil_image = Image.fromarray(thresh_image)

extracted_text = pytesseract.image_to_string(pil_image)

print(extracted_text)

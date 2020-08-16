#coding=utf-8
import pytesseract
from PIL import Image
image = Image.open('F:\\learn\\selenium\\one.png')
text = pytesseract.image_to_string(image)
print(text)
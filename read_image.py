#coding=utf-8
import pytesseract
from PIL import Image
image = Image.open('C:\\Users\\Administrator\\Desktop\\imooc_selenium\\one.png')
text = pytesseract.image_to_string(image)
print(text)
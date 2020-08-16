#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("C:/imooc.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("C:/imooc.png")
img = im.crop((left,top,right,height))
img.save("C:/imooc1.png")


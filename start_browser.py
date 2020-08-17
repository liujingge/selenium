#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("F:\\learn\\selenium\\imooc1.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("F:\\learn\\selenium\\imooc1.png")
img = im.crop((left,top,right,height))
img.save("F:\\learn\\selenium\\imooc1.png")

r = ShowapiRequest("http://route.showapi.com/1274-2","my_appId","my_appSecret" )
r.addBodyPara("imgUrl", "")
r.addBodyPara("base64", "")
r.addFilePara("imgFile", r"F:\\learn\\selenium\\imooc1.png")#文件上传设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(5)
driver.find_element_by_id("captcha_code").send_keys(text)



driver.find_element_by_class_name("controls")
locals = (By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

print(email_element.get_attribute("placeholder"))
email_element.send_keys("123@qq.com")


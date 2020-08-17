#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
# image = Image.open('F:\\learn\\selenium\\imooc1.png')
# text = pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/1274-2","my_appId","my_appSecret" )
r.addBodyPara("imgUrl", "")
r.addBodyPara("base64", "")
r.addFilePara("imgFile", r"F:\\learn\\selenium\\imooc1.png")#文件上传设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
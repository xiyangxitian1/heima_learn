from PIL import Image
import pytesseract  # 文字识别的库
import subprocess

image = Image.open('1.jpg')
image = image.point(lambda x: 0 if x < 220 else 255)  # 低于143为黑色 否则为白色
image.save('123.png')


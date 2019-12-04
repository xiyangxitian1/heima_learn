from PIL import Image
import pytesseract  # 文字识别的库
import subprocess

image = Image.open('2.jpg')
num = pytesseract.image_to_string(image)
print(num)

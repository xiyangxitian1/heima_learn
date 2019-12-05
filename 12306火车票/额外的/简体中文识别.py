from PIL import Image
import pytesseract  # 文字识别的库
import subprocess

image = Image.open('3.jpg')
text = pytesseract.image_to_string(image, lang='chi_sim') # 可以识别了
print(text)

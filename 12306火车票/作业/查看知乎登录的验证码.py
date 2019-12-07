from PIL import Image
import pytesseract  # 文字识别的库
import subprocess

image = Image.open('1.jpg')
tessdata_dir_config = '--tessdata-dir "D:/ly/Tesseract-OCR/tessdata"'

text = pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)
print(text)

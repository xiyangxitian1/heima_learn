from PIL import Image
import time

img = Image.open('1.jpg')
img.show()
time.sleep(5)
img.close()

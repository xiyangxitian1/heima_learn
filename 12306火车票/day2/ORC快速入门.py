#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ORC快速入门.py
# Author: MuNian
# Date  : 2019-12-04


import pytesseract
from PIL import Image


image = Image.open('tess2.png')
text = pytesseract.image_to_string(image)
print(text)




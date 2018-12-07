#!/usr/local/bin/python
# -*-coding:utf-8-*-

import pytesseract
from PIL import Image

code = pytesseract.image_to_string(Image.open('th.jpg'))
print code

class ValidateCodeHandler:
    pass



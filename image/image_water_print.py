#!/usr/local/bin/python
# -*-coding:utf-8-*-
import re

import pytesseract
from PIL import Image
import subprocess


class HandlerImageWater:

    def clearnFile(self, filePath, newFilePath):
        """处理图片背景色，使图片更清晰可识别"""

        image = Image.open(filePath)

        # 对图片进行阀值过滤，然后保存
        image = image.point(lambda x: 0 if x < 143 else 255)
        image.save(newFilePath)

        # 调用系统的tesseract命令对图片进行ocr识别
        subprocess.call(["tesseract", newFilePath, "output"])

        # 打开文件读取结果
        output_file = open("output.txt", 'r')
        print output_file.read()
        output_file.close()

    def randomCodeOcr(self, filename):
        image = Image.open(filename)
        # 使用ImageEnhance可以增强图片的识别率
        # enhancer = ImageEnhance.Contrast(image)
        # enhancer = enhancer.enhance(4)
        image = image.convert('L')
        ltext = ''
        ltext = pytesseract.image_to_string(image)
        # 去掉非法字符，只保留字母数字
        ltext = re.sub("\W", "", ltext)
        print u'[%s]识别到验证码:[%s]!!!' % (filename, ltext)
        image.save(filename)
        # print ltext
        return ltext


obj = HandlerImageWater()
# obj.clearnFile("text.png", "text_2_clean.png")
# obj.clearnFile("validate-code-01.jpg", "validate-code-01-clearn.jpg.png")
obj.randomCodeOcr('vc1.png')
#!/usr/bin/python
# -*-coding:utf-8-*-

'''
python 图片处理工具类
'''
import os

from PIL import Image, ImageDraw, ImageFont


class ImageParser:
    def img_basic(self):
        img = Image.open('answer1.png')
        width, height = img.size
        print width, height
        print 'filename:%s' % img.filename
        # print 'filetype: %a' % img.format
        # print 'desc: %s' % img.file_description

    def new_img(self):
        #  紫色背景
        img = Image.new('RGBA', (100, 200), 'purple')
        img.save('test.png')
        # 没有背景
        img2 = Image.new('RGBA', (20, 20))
        img2.save('test2.png')

    # 复制和粘贴图像到其他图像
    def cover_img(self):
        img = Image.open('answer1.png')
        copy_img = img.copy()

        face_img = img.crop((335, 345, 565, 560))
        print face_img.size

        copy_img.paste(face_img,(0, 0))
        copy_img.paste(face_img,(400, 500))
        copy_img.save('pasted.png')

    def draw_image(self):
        img = Image.new('RGBA', (200, 200), 'white')
        draw = ImageDraw.Draw(img)
        # 给图片边缘画上窄的黑色轮廓
        draw.line([(0, 0),(199, 0),(199, 199),(0, 199)], fill='black')
        # 矩形
        draw.rectangle(((20, 30, 60, 60)), fill='blue')
        # 椭圆
        draw.ellipse((120, 30, 160, 60), fill='red')
        # 多边形
        draw.polygon(((57, 87),(79, 62),(94,85),(120,90),(103,113)),fill='brown')
        for i in range(100,200,10):
            draw.line([(i,0),(200,i-100)], fill='green')
        img.save('drawing.png')

    def draw_txt_on_img(self):
        img = Image.new('RGBA', (200, 200), 'white')
        draw = ImageDraw.Draw(img)
        draw.text((20,150),'hello',fill='purple')
        fontsFolder ='C:\Windows\Fonts'
        arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'Arial.ttf'),32)
        draw.text((100,150),'Howdy',fill='gray',font=arialFont)
        img.save('text.png')

if __name__ == '__main__':
    obj = ImageParser()
    obj.draw_txt_on_img()
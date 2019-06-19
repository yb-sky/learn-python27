#!/usr/bin/python
# -*-coding:utf-8-*-

from PIL import Image
import pytesseract

class ImagerParser:
    tessdata_dir_config = '--tessdata-dir "d:\Soft\Tesseract-OCR/tessdata"'

    # 二值图处理
    def binarizing(self, img ,threshold):
        pixdata =img.load()
        print(pixdata)
        # 加载的图片宽和高
        w , h =img.size
        print (w ,h)
        for y in range(h):
            for x in range(w):
                print(pixdata[x ,y])
                if pixdata[x ,y ] <threshold:
                    pixdata[x ,y ] =0
                else:
                    pixdata[x ,y ] =255
        return img

    ###########去除干扰线算法
    def depoint(self, img):  # input: gray image
        pixdata = img.load()
        w ,h = img.size
        for y in range(1 , h -1):
            for x in range(1 , w -1):
                count = 0
                print(pixdata[x, y - 1])
                if pixdata[x , y -1] > 245:
                    count = count + 1
                if pixdata[x , y +1] > 245:
                    count = count + 1
                if pixdata[ x -1 ,y] > 245:
                    count = count + 1
                if pixdata[ x +1 ,y] > 245:
                    count = count + 1
                if count > 2:
                    pixdata[x ,y] = 255
        return img


if __name__ == '__main__':
    obj = ImagerParser()

    img = Image.open('th.jpg')
    # 原图片展示
    img.show()
    # 保存图片
    # img.save("th.jpg")
    # 必须转化为灰度图，否则，后面会报错TypeError: '<' not supported between instances of 'tuple' and 'int'
    img_grey = img.convert('L')
    img_grey.show()
    # 保存图片
    img_grey.save("th_grey.png")
    # 调用函数，以190像素为界限
    # new_img=binarizing(img_grey,190)
    # new_img.save("new_img_3.png")

    new_img = obj.depoint(img_grey)
    new_img.save("new_img_31.png")

    # 识别图片
    code = pytesseract.image_to_string(new_img ,config=obj.tessdata_dir_config)
    print(code)

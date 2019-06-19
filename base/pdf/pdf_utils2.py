#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import os.path
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

class HandlerPdf:
    def __init__(self):
        '''''
        Constructor
        '''''

    def readPdf(self, filePath):
        self.result = ''

        # 二进制读取文件
        file = open(filePath, 'rb')
        # pdf解析器
        parser = PDFParser(file)
        # pdf文档
        doc = PDFDocument(parser)
        # 检测文档是否提供text转换
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed

        # 连接解析器和文档对象
        # parser.set_document(doc)
        # doc.set_parser(parser)
        # 提供初始密码
        # 没有密码创建一个空字符串
        # doc.initialize()

        # 创建pdf资源管理器
        resource_manager = PDFResourceManager()
        # pdf设备对象
        laparams = LAParams()
        device = PDFDevice(resource_manager)
        device = PDFPageAggregator(resource_manager, laparams=laparams)
        # pdf解释器
        interpreter = PDFPageInterpreter(resource_manager, device)
        pdf_str = ''
        # 遍历列表，每次处理一个page内容

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            layout = device.get_result()
            for row in layout:
                if hasattr(row, "get_text"):
                    self.result = self.result + (str(row.get_text())) + '\n'

                    # if (isinstance(row, LTTextBoxHorizontal)):
                    #     with open('a.txt', 'a') as f:
                    #         f.write(row.get_text().encode('utf-8') + '\n')

        fileNames = os.path.splitext(filePath)
        if os.path.exists(fileNames[0] + '.txt'):
            return

        with open(fileNames[0] + '.txt', 'a') as f:
            f.write(self.result)

    def get_dir_files(self, dir):
        files = dict()
        counter = 0
        for parent, dirnames, filenames in os.walk(dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for filename in filenames:  # 输出文件信息
                # counter = counter + 1
                # if counter > 1:
                #     break

                full_name = os.path.join(parent, filename)
                if not 'pdf' in full_name:
                    continue

                print('Read %s' % full_name)
                self.readPdf(full_name)

    def man(self):
        start_time = time.time()

        path = u'E:\doc\Books\Credit\卡研社'
        self.get_dir_files(path)

        end_time = time.time()
        print('耗时：%d' % (end_time - start_time))

if __name__ == '__main__':
    obj = HandlerPdf()
    obj.man()

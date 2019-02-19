#!/usr/bin/python
#-*-coding:utf-8-*-

'''
操作pdf文件类
'''

# from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPdf(pdfFile):
    resourceManage = PDFResourceManager()
    strIO = StringIO()
    laparams = LAParams()
    txtConverter = TextConverter(resourceManage,strIO,laparams)
    process_pdf(strIO, txtConverter, pdfFile)
    txtConverter.close()

    content = strIO.getvalue()
    strIO.close()
    return content

# pdfFile = urlopen('E:\\doc\\Books\\Credit\\卡研社\\POS 机 Q&A.pdf')
pdfFile = open('E:\\doc\\Books\\Credit\\卡研社\\POS 机 Q&A.pdf')
res = readPdf(pdfFile)
print(res)
pdfFile.close()

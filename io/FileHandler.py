#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import os

''''' 
文件读写操作
Created on 2018年6月27日  
@author: SkyOne 
link: http://www.runoob.com/python/python-files-io.html

with语句打开和关闭文件，包括抛出一个内部块异常。

'''

class FileHandler:
    def readFile(self,path):
        with open(path,'r') as f:
            for line in f.readlines():
                return (line.strip())

    def writeFile(self,path,content):
        with open(path,'a') as f:
            f.write(content)

    def readConsole(self):
        str = raw_input("请输入：")
        print "你输入的内容是：", str

        # str = input("请输入：")
        # print "你输入的内容是：", str

        return str

    files = []
    # 递归方法读取文件夹下面的文件
    def getDirFiles(self,path):
        fileList = os.listdir(path)
        for f in fileList:
            fpath = os.path.join(path,f)
            # print fpath
            if os.path.isdir(fpath):
                self.getDirFiles(fpath)

            self.files.append(fpath)
        return self.files

    # 递归方法读取文件夹下面的文件, os模块的walk（）函数实现
    # os.walk(top, topdown=True, onerror=None, followlinks=False)
    # 返回一个3个元素的元祖，(dirpath, dirnames, filenames),
    # dirpath：要列出指定目录的路径
    # dirnames：目录下的所有文件夹
    # filenames：目录下的所有文件
    # 参数一：top – 根目录下的每一个文件夹(包含它自己), 产生3 - 元组(dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
    # 参数二：topdown –可选，为True或者没有指定, 一个目录的的3 - 元组将比它的任何子文件夹的3 - 元组先产生(目录自上而下)。如果topdown为
    # False, 一个目录的3 - 元组将比它的任何子文件夹的3 - 元组后产生(目录自下而上)。
    # 参数三：onerror – 可选，是一个函数;
    # 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk, 或者抛出exception终止walk。
    # 参数四：followlinks – 设置为
    # true，则通过软链接访问目录。
    def getDirFilesMoreQuick(self,path):
        for root,dirs,fls in os.walk(path,topdown=False):
            # for dir in root:
            #     print dir
            for name in dirs:
                self.files.append(os.path.join(root,name))
            for name in fls:
                self.files.append(os.path.join(root, name))
            return self.files

if __name__ == '__main__':
    fileHandler = FileHandler()

    path = 'd:\\test.txt'

    data = fileHandler.readConsole()
    fileHandler.writeFile(path,data)
    #
    # content = fileHandler.readFile(path)
    # print content
    #
    # # files = fileHandler.getDirFiles("D:\\VM")
    # files = fileHandler.getDirFilesMoreQuick("d:\\vm")
    # print('files:',files)





#!/usr/bin/python
# -*-coding:utf-8-*-

'''
os: 处理文件|路径模块
模块
    os.getcwd()：查看当前所在路径。
    os.listdir(path):列举目录下的所有文件。返回的是列表类型。
    os.path.abspath(path):返回path的绝对路径
    os.path.split(path):将路径分解为(文件夹,文件名)，返回的是元组类型
    os.path.join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除
    os.path.dirname(path):返回path中的文件夹部分，结果不包含'\'
    os.path.basename(path):返回path中的文件名。

    os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
    os.path.getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数。
    os.path.getctime(path):文件或文件夹的创建时间，从新纪元到访问时的秒数

    os.path.getsize(path):文件或文件夹的大小，若是文件夹返回0
    os.path.exists(path):文件或文件夹是否存在，返回True 或 False
    os中定义了一组文件、路径在不同操作系统中的表现形式参数（os.sep '\\'、os.extsep '.'、os.pathsep ';'、os.linesep '\r\n'）


'''

import os

path = u'E:\\doc\\Books\\Credit\\卡研社\\'
path_ = os.path.dirname(path)
print(path_)

def list_dir_file1():
    for row in os.listdir(path):
        print(row)
        print(path_ + '\\' + row)

def list_dir_file(rootdir):
    files = dict()
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        print('parent', parent)
        print('dirnames', dirnames)
        print('filenames', filenames)

        for dirname in dirnames:  # 输出文件夹信息
            print "parent is:" + parent
            print "dirname is" + dirname

        for filename in filenames:  # 输出文件信息
            print "parent is:" + parent
            print "filename is:" + filename
            print "the full path is:" + os.path.join(parent, filename)  # 输出文件路径信息
            files[filename] = os.path.join(parent, filename)

    return(files)

files = list_dir_file(path)
print(type(files))
for key, val in files.items():
    key_ = key
    print(key_)
    print(val)
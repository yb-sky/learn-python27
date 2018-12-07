#!/usr/bin/python
# -*-coding:utf-8-*-
import os
import shutil
import sys

"""
文件处理帮助类
"""

def write_file(path, content):
    """
    追加方式写入文件
    :param path: 文件绝对路径
    :param content:  写入文件内容
    :return:
    """
    with open(path, 'a+') as f:
        f.write(content)


def read_file(path):
    """
    读取文件
    :param path: 文件绝对路径
    :return:   文件全部内容
    """
    with open(path, 'r+') as file:
        return file.readlines()


def copy_file(source, dest):
    """
    shutil.copy(src, dst)：复制文件src到文件或目录dst。如果dst是目录，使用src相同的文件名创建（或覆盖），权限位也会复制。src和dst的是字符串形式的路径名。
    shutil.copyfile(src, dst)：复制文件内容（不包含元数据）从src到dst。 DST必须是完整的目标文件名;
        如果src和dst是同一文件，就会引发错误shutil.Error。dst必须是可写的，否则将引发异常IOError。如果dst已经存在，它会被替换。
    :param source:
    :param dest:
    :return:
    """
    shutil.copy(source, dest)


def delete_file(path):
    """
    :desc 删除文件
    :param path:
    :return:
    """
    if os.path.exists(path):
        os.remove(path)

def move_file(src, dst):
    shutil.move(src, dst)

# 控制台获取文件名
def get_fileName(fileDesc):
    print('输入0退出程序')
    filename = str(input("输入%s文件名: " % fileDesc))

    while 1:
        if len(filename) == 0:
            filename = str(input("输入%s文件名: " % fileDesc))
        elif int(filename) == 0:
            sys.exit()
        else:
            break

    print('您输入的文件名是：%s' % filename)
    return filename


#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path

def get_dir_files(dir):
    files = dict()
    for parent, filenames in os.walk(dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:  # 输出文件信息
            files[filename] = os.path.join(parent, filename)
    return(files)
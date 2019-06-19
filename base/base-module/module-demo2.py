#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mymodule

"""
警告：要记住你应该避免使用 import 这种形式，即	`from	mymodule	import	`
from	mymodule	import	* 不会导入__version__,只会导入公共方法
dir 函数： 内置的dir()函数能够返回由对象所定义的名称列表
    在默认情况下，它将返回当前模块的属性列表
"""
mymodule.say_hi()
print('version', mymodule.__version__)

# from..import
from mymodule import say_hi, __version__
say_hi()
print __version__

def func_dir():
    import sys
    for row in dir(sys):
        print row

func_dir()
print dir(str)
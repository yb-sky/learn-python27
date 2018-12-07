#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
类-Class
    字段：从属于对象或类的变量叫作字段（Field）
        字段有两种类型——它们属于某一类的各个实例或对象，或是从属于某一类本身。它们被分别称作实例变量（Instance	Variables）与类变量（Class	Variables）
    方法：用属于类的函数来实现某些功能，这种函数叫作类的方法（Method）
    字段与方法通称类的属性（Attribute）

对象-Object
    1. 对象（Object）就是类的实例（Instance）
self
    1. 你需要记住你只能使用	 	 self		来引用同一对象的变量与方法。这被称作属性引用（AttributeReference）
"""
class ClazzDemo:
    def __init__(self):
        pass

print ClazzDemo.__doc__
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

"""
测试异常
"""
# print(help('raise'))
print(__doc__)

def throwErr():
    raise Exception("抛出一个异常")

throwErr()
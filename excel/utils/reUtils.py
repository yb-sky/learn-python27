#!/usr/bin/python
# -*-coding:utf-8-*-

import re

"""
    desc: 正则工具类
"""


def remove_chinese(raw):
    """
    :desc: 清除中文字符,保留字母、数字、标点符号
    :param raw:
    :return:
    """
    fil = re.compile(ur'[^0-9a-zA-Z\u4e00-\u9fa5.，,。？“” \- / ]+', re.UNICODE)
    return fil.sub('', raw)
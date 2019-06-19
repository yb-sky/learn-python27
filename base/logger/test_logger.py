#!/usr/local/bin/python
# -*-coding:utf-8-*-

# 参考：https://docs.python.org/2/library/logging.config.html

import logging

logging.basicConfig(level=logging.DEBUG)

fmt = '%(levelname)s:%(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(fmt))
logging.getLogger().addHandler(console_handler)

logging.info('hello!')

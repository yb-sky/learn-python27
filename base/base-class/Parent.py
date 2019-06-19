#!/usr/bin/python
# -*- coding: UTF-8 -*-

""""
  类和实例基本特性：实例对象属性和方法是各自独立的，互不影响。
  继承： 子类继承父类变量或属性，都指向相同的内存地址。除非子类改变属性值。
"""
class Parent(object):

    x = 1


class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x

Child1.x = 2
print Parent.x, Child1.x, Child2.x

Parent.x = 3
print Parent.x, Child1.x, Child2.x

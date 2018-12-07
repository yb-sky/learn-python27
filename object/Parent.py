#!/usr/bin/python
# -*- coding: UTF-8 -*-

class People:
    def __init__(self):
        print '人类'

    def displayName(self):
        print '调用父类方法: displayName'

class Parent:    # 定义父类

    def __init__(self):
        print '类的继承'

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr

    if __name__ == '__main__':
        print '----------类的继承示例：------------'

# 继承多个父类
class Child(People,Parent):
    def __init__(self):
        print ' 调用子类构造方法'

    def childMethod(self):
        print '调用子类方法'

    def displayName(self):
        print '调用子类方法: displayName'


c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值

# 方法重写
c.displayName()
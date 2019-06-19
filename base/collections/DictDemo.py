#!/usr/bin/python
#-*-coding:utf-8-*-

'''''
数据库操作工具类
Created on 2018年7月4日
@author: SkyOne
'''
#
# 字典(dict)转为字符串(string)
#
# 我们可以比较容易的将字典(dict)类型转为字符串(string)类型。
#
# 通过遍历dict中的所有元素就可以实现字典到字符串的转换：
#
# for key, value in sample_dic.items():
#     print "\"%s\":\"%s\"" % (key, value)
#
# 字符串(string)转为字典(dict)
#
# 如何将一个字符串(string)转为字典(dict)呢?
#
# 其实也很简单，只要用 eval()或exec() 函数就可以实现了。
#
# >>> a = "{'a': 'hi', 'b': 'there'}"
# >>> b = eval(a)
# >>> b
# {'a': 'hi', 'b': 'there'}
# >>> exec ("c=" + a)
# >>> c
# {'a': 'hi', 'b': 'there'}
# >>>
class DictDemo:
    def test(self):
        sc = dict([('a', 'ab'), ('b', 'b')])
        for key in sc.keys():
            print(key)

    def test2(self):

        sc = dict([('a','ab'),('b','b')])
        for key in sc.keys():
            print(key)

        for key,val in sc.items():
            print(key,val)

        print(sc.__contains__('a'))

        d = dict()
        for i in range(3):
            d[str(i)] = i + 30

        print len(d)
        print(d.__contains__('1'))
        print(d.get('1'))

    def foo(var):
        return {
            '1': '一',
            '2': '二',
            '3': '三',
            '4': '四',
            '5': '五',
            '6': '六',
        }.get(var,'error')

    def do_iterator(self):
        d = {'x': 'A', 'y': 'B', 'z': 'C'}

        print [k + '=' + v for k, v in d.iteritems()]

        for k, v in d.iteritems():
            print k, v
print help(dict)
obj = DictDemo()
obj.do_iterator()
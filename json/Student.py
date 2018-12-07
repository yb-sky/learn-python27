#!/usr/bin/python
#-*-coding:utf-8-*-

import json
print (json.__all__) #查看json库的所有方法
'''
说明：Python类对象的JSON序列化处理
作者：SkyOne
'''

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def obj2json(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

    def json2obj(self):
        str = '{"age": 20, "score": 80, "name": "test"}'
        result = Student(**json.loads(str))

        print result.name

class Employee:
    name = ''
    age = 0
    income = 0
    addr = ''

    # def __init__(self,name,age,income):
    #     name = name
    #     age = age
    #     income = income

    def obj2json(std):
        return {
            'name': std.name,
            'age': std.age,
            'income': std.income,
            'addr': std.addr
        }

    def test(self):
        str = '{"age": 20, "income": 8000, "name": "test", "addr": "hunanchangshai"}'
        print(json.dumps(str, default=self.obj2json))

if __name__ == '__main__':
    # s = Student('test', 20, 80)
    # print(json.dumps(s, default = Student.obj2json))
    # s.json2obj()

    Employee().test()
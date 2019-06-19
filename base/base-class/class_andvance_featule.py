#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
"""


class Student(object):
    pass


def set_age(self, age):
    self.age = age


s = Student()
s.name = "bluesky"
print s.name

# 动态添加方法
from types import MethodType

s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法,给一个实例绑定的方法，对另一个实例是不起作用的
s.set_age(23)
print s.age


# 给class绑定方法，所有实例均可调用
def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, None, Student)
s.set_score(99)
print s.score


class Teacher(object):
    # __slots__ = ('name', 'age')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if not isinstance(val, int):
            raise ValueError('age must be an integer')
        if val < 0 or val > 100:
            raise ValueError('score must  between 0-120')
        self._age = val


t = Teacher()


def set_score(self, score):
    self.score = score


Teacher.set_score = MethodType(set_score, None, Teacher)

# 如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
t.age = 34
t.name = "blueSky"
# t.score = 98
print t.age, t.name

t.age = 99
print t.age

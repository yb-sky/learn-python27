#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    函数：指可以重复使用的程序判断。
    形参：定义函数时给定的名称
    实参：调用函数时提供的指称"作实参"
    变量只存在于函数这一局部被称为变量的作用域
    global:语句用以声明 x是一个全局变量——因此，当我们在函数中为 x进行赋值时，这一改动将影响到我们在主代码块中使用的x的值
    参数默认值：只有那些位于参数列表末尾的参数才能被赋予默认参数值，意即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前
    关键字参数
    可变参数：* 表示数组，** 表示数组
"""

print(__doc__)
print(__name__)

def say_hello():
    print('hello world')

x = 50
def func_local_variable(x):
    print('x is ', x)
    x = 2
    print('change local x to ', x)

def func_global_variable():
    global x
    print('x is ', x)
    x = 2
    print('change local x to ', x)

def func_default_val(message, times=1):
    print message * times

def func_varargs(a=4, *arry, **dicts):
    print 'a=%d' % a

    # 遍历元组中所有项目
    for item in arry:
        print 'item ', item

    # 遍历字典中的项目
    for first_part, second_part in dicts.items():
        print first_part, second_part

def func_return():
    '''
    默认返回None
    :return:
    '''
    pass


# func_global_variable()
# print 'value of x is ', x

# func_varargs(10,1,2,3,jack=1123,john=2123,inge=321)
print(func_return()) #None
help(func_return)

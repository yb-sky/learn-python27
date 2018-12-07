#!/usr/bin/python
#-*-coding:utf-8-*-

#元组也是一个list，他和list的区别是元组的元素无法修改
tuple1 = (2,3,4,5,6,4,7)
print(type(tuple1))
print(tuple1[:7])
print(tuple1[:5:-1])
for i in range(7):
    print('t:%d',tuple1[i])

print('\n')
for i in tuple1:
    print(type(i))
    print('i: %d',i)
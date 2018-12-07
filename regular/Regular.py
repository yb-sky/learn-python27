#!/usr/bin/python
#-*-coding:utf-8-*-

# 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
# re 模块使 Python 语言拥有全部的正则表达式功能。
# compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。

import re

# 在起始位置匹配
print(re.match('www','www.runoob.com').span())
# result: (0, 3)

print('aaa ', re.match('\d+', '04/103焊肩片').span())

print('bbb ',re.match('\d+', 'T-04/103焊肩片'))

# 不在起始位置匹配
print(re.match('com', 'www.runoob.com'))
# result: None

print "\n"

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符
# (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符
# (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，只匹配符合条件的最少字符
# 后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中

if(matchObj):
    print "matchObj.group():",matchObj.group()  #表示匹配到的完整文本字符
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
    # print "matchObj.group(2) : ", matchObj.group(3) # 报错， no such group 没有找到分组
else:
    print "No match!"


# 字符串中匹配数字
def find_num():
    # \d+ 匹配字符串中的数字部分，返回列表

    ss = 'adafasw12314egrdf5236qew'
    num = re.findall('\d+', ss)
    print(num)
    # 运行结果
    # ['12314', '5236']
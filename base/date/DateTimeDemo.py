#!/usr/bin/python
#-*-coding:utf-8-*-

import datetime
import time

# print (time.__all__) #查看json库的所有方法

class DateTimeDemo:
    def datetime_demo(self):
        i = datetime.datetime.now()
        print ("当前的日期和时间是 %s" % i)
        print ("ISO格式的日期和时间是 %s" % i.isoformat())
        print ("当前的年份是 %s" % i.year)
        print ("当前的月份是 %s" % i.month)
        print ("当前的日期是  %s" % i.day)
        print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
        print ("当前小时是 %s" % i.hour)
        print ("当前分钟是 %s" % i.minute)
        print ("当前秒是  %s" % i.second)

        strtime1 = '20160518010101'


    def time_demo(self):
        print time.localtime()

        # 格式化成2016-03-20 11:45:39形式
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 格式化成Sat Mar 28 22:24:24 2016形式
        print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

        # 将格式字符串转换为时间戳
        a = "Sat Mar 28 22:24:24 2016"
        print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

    def time_date_demo(self):
        strtime1 = '20160518010101'
        strtime2 = '20160518020101'
        time3 = '1/1/2015'.replace('/','-')
        print time3

        # 字符串变成时间数据结构
        localtime1 = time.strptime(strtime1, '%Y%m%d%H%M%S')
        localtime2 = time.strptime(strtime2, '%Y%m%d%H%M%S')
        localtime3 = time.strptime(time3, '%d-%m-%Y')

        print type(localtime1), localtime1.tm_year,localtime1.tm_mon
        print type(localtime2), localtime2.tm_year,localtime2.tm_mon
        print localtime3.tm_year,localtime3.tm_mon

        # 从时间数据结构转换成时间戳
        time1 = time.mktime(localtime1)
        time2 = time.mktime(localtime2)
        print time1,time2

if __name__ == '__main__':
    obj = DateTimeDemo()
    obj.datetime_demo()





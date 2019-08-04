#!/usr/bin/python
#-*-coding:utf-8-*-

import MySQLdb

''' 
pip2 install MySQL-python

1. 获取所有学校
2. 获取每所学校下的老师、学生信息
'''

class ZhxDataDown:
    # conn = None 
    # cursor = None 

    def __init__(self,host='localhost',name='',pwd='',dbName='accountdb_cloud_',port=13306):
        self.host = host
        self.name = name
        self.pwd = pwd
        self.dbName = dbName
        self.port = port
        self.conn = MySQLdb.connect(host,name,pwd,dbName,charset='utf8')
        self.cursor = self.conn.cursor()

    def query_shcool(self):
        print('query scool')
        try:
            self.cursor.execute('select count(*) from t_school')
            data = self.cursor.fetchone()
            print(data)
        except expression as identifier:
            pass

if __name__ == "__main__":
    obj = ZhxDataDown()
    obj.query_shcool()
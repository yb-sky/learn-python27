#!/usr/bin/python
#-*-coding:utf-8-*-

# DB-API 是一个规范. 它定义了一系列必须的对象和数据库存取方式, 以便为各种各样的底层数据库系统和多种多样的数据库接口程序提供一致的访问接口 。
#
# Python的DB-API，为大多数的数据库实现了接口，使用它连接各数据库后，就可以用相同的方式操作各数据库。
#
# Python DB-API使用流程：
#
# 引入 API 模块。
# 获取与数据库的连接。
# 执行SQL语句和存储过程。
# 关闭数据库连接。

# MySQLdb 是用于Python链接Mysql数据库的接口，它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。

# 错误处理
# DB API中定义了一些数据库操作的错误及异常，下表列出了这些错误和异常:

# 异常	描述
# Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
# Error	警告以外所有其他错误类。必须是 StandardError 的子类。
# InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
# DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
# DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
# OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
# IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
# InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
# ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
# NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。

import MySQLdb
''''' 
数据库操作工具类
Created on 2018年6月27日  
@author: SkyOne 
'''

class DBHelper:
    # 数据库连接
    __conn = None
    __cursor = None

    def __init__(self,host='localhost',name='root',pwd='root',dbName='test',port=3306):
        self.host = host
        self.name = name
        self.pwd = pwd
        self.dbName = dbName
        self.port = port
        self.__conn = MySQLdb.connect(host,name,pwd,dbName,charset='utf8') #打开数据库连接
        self.__cursor = self.__conn.cursor() # 使用cursor()方法获取操作游标

    def getDBVersion(self):
        cursor = self.__cursor
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchone()
        print "Database version: : %s" % data
        return data

    def closeDb(self):
        # 关闭数据库连接
        self.__conn.close()

    def createDataBase(self,dbName,sql):
        cursor = self.__cursor
        cursor.execute("drop table if EXISTS " % dbName)
        cursor.execute(sql)
        data = cursor.fetchone()
        print "createDataBase : %s" % data
        return data

    def save(self,sql):
        cursor = self.__cursor

        print(sql)
        try:
            cursor.execute(sql)
            self.__conn.autocommit()
        except:
            # self.__conn.rollback()
            print "执行%s报错" % sql

        self.closeDb()

    def query(self,sql):
        cursor = self.__cursor
        try:
            cursor.execute(sql)
            results = cursor.fetchall()

            print(results)

            data = None
            for row in results:
                print(row[0],row[1],row[2],row[3],row[4])

            print data
        except:
            print "Error: execute %s" % sql

    def update(self,sql):
        cursor = self.__cursor
        try:
            cursor.execute(sql)
            self.__conn.autocommit()
        except:
            print "Error: execute %s" % sql


db = DBHelper('localhost','root','root','test',3306)
# version = db.getDBVersion()

# Insert
insert_sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', %d, %d, %d )" % \
      ('Mac', 'Mohan', 20, 1, 2000)
# db.save(insert_sql)

# WHERE SEX = '%d'" % (1)
update_sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 "
db.update(update_sql)

query_sql = """
    select * from employee 
"""
db.query(query_sql)


create_sql = """
       create table employee(
    first_name VARCHAR(20) not null,
    last_name VARCHAR(20),
    age int ,
    sex int ,
    income float
   )
   """
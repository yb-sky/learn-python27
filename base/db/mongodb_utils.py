#!/usr/bin/python
#-*-coding:utf-8-*-

from pymongo import MongoClient

class MongoUtils:
    __client = None

    def __init__(self):
        self.__client = MongoClient('127.0.0.1', 27017)

    def do_query(self):
        cli = self.__client
        # create database
        db = cli.test_db
        # create collections
        coll = db.test_col

        coll.insert({"name":"python","version":"2.7"})
        coll.insert([{"name":"mongodb","version":"v4.0.0-73-g4687ff2c13"},
                     {"name": "mysql", "version": "5.6"}])
        print(db,coll)

        # 查找     find第一个参数表示条件,第二个表示结果显示内容
        res = coll.find({"name": "mongodb"})
        print(res)
        # res = coll.find({"name": "mongodb"}, {"name": 1, "age": 1})
        ress = coll.find()
        for data in ress:
            print(data)

        print(res)

    def test(self):
        print('test()')

if __name__ == '__main__':
    obj = MongoUtils()
    obj.do_query()



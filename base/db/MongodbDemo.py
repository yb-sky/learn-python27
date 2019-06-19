#!/usr/bin/python
#-*-coding:utf-8-*-

import pymongo

class MongoDbDemo:
    __client = None

    def __init__(self):
        self.__client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

    def exist_db(self, name):
        client = self.__client
        dblist = client.list_database_names()
        print('数据库：' % dblist)
        for db in dblist:
            print(db)
        if name in dblist:
            print(name+'数据库已经存在!')
            return True

        return False

    def list_collections(self):
        client = self.__client['yueting']
        collections = client.collection_names()
        for coll in collections:
            print(coll)

    def do_save(self, data):
        client = self.__client['yueting']
        col = client['auto_learning']
        # if type(data).__name__ == 'list':
        #     res = col.insert_many(data)
        #     print('Inserted many record: '+res.inserted_ids)
        # else:
        #     res = col.insert_one(data)
        #     print('Inserted one record: '+res.inserted_id)
        res = col.insert(data)
        print(res)

    def db_delete(self, name):
        client = self.__client['yueting']
        col = client['auto_learning']
        if name is not None:
            print col.remove(name)
        else:
            print col.remove()

    def test(self):
        data = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
        datas = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 20}]
        print(type(datas))
        # self.do_save(datas)
        self.db_delete({'name': 'zhangsan'})
        self.db_delete(None)

if __name__ == '__main__':
    db = MongoDbDemo()
    # db.exist_db('yueting')
    # db.list_collections()
    db.test()

    mylist = [
        {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ]
    print(type(mylist).__name__ == 'list')
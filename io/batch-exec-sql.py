#!/usr/bin/python
# -*-coding:utf-8-*-
import datetime

import MySQLdb
# import psycopg2
import sys

reload(sys)
sys.setdefaultencoding('utf8')

'''
批量执行sql文件
1. 读取sql文件
2. 循环每读取1000行，执行sql
3. 执行余下的sql
'''


class ExecSQL:
    def __init__(self):
        # self.conn = psycopg2.connect(dbname='ycl_resource', user='root', password='pangu', host='127.0.0.1', port=5432)
        # self.cursor = self.conn.cursor()
        self.conn = MySQLdb.connect(host='127.0.0.1', user='yuncl', passwd='yuncl@Zuoyetong_2014', db='yuncelian', port=13306, charset='utf8')
        self.cursor = self.conn.cursor()

    def __get_param(self):
        path = raw_input('请输入sql文件路径：')
        count = int(raw_input('请输入批量执行数量：'), 10)
        if not isinstance(count, int):
            print("批量执行数量 not int类型, 请重输")
            count = raw_input('请输入批量执行数量：')
        if not isinstance(count, int):
            return None
        return (path, count)


    def load_and_exec_sql(self, path, size):
        print '开始执行%s' % path
        counter = 1
        sql = ''
        count = 0
        start_time = datetime.datetime.now()

        with open(path, 'r+') as f:
            datas = f.readlines()
            print '总记录数为：%d' % len(datas)

            for line in datas:
                if counter % size == 0:
                    # 批量执行sql语句
                    print sql
                    try:
                        self.cursor.executemany(sql)
                        self.conn.commit()
                    except Exception as e:
                        self.conn.rollback()
                        print("执行MySQL时出错：%s" % e)
                        self.writeFile('error-sql.txt', sql)

                    counter = 1
                    sql = ''
                    count += 1
                    print 'exec %d' % count
                else:
                    sql += line
                    counter += 1
            try:
                if len(sql) > 0:
                    self.cursor.execute(sql)
                    self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print("执行MySQL时出错：%s" % (e))
                self.writeFile('error-sql.txt', sql)

            self.cursor.close()
            self.conn.close()

            end_time = datetime.datetime.now()
            print '执行结束,耗时 %s' % str(end_time - start_time)


    def read_file(self, path):
        with open(path, 'r+') as file:
            for line in file.readlines():
                print line


    def exec_single_sql(self, path):
        print '开始执行%s' % path
        start_time = datetime.datetime.now()
        with open(path, 'r+') as f:
            datas = f.readlines()
            print '总记录数为：%d' % len(datas)
            sql = datas[0]
            # print sql
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print("执行SQL时出错：%s" % (e))
            # finally:
            #     self.cursor.close()
            #     self.conn.close()

        end_time = datetime.datetime.now()
        print '执行结束,耗时 %s' % str(end_time - start_time)


    def writeFile(self, path, content):
        with open(path, 'a') as f:
            f.write(content)


if __name__ == '__main__':
    obj = ExecSQL()
    # path = 'student/insert_student_2.sql'
    # for i in range(1, 538):
    #     path = 'update_student/update_student_shoolid_%d.sql' % i
    #     print 'Start exec: %s' % path
    #     obj.exec_single_sql(path)

    for i in range(1, 538):
        path = 'update_student/update_student_shoolid_%d.sql' % i
        print 'Start exec: %s' % path
        obj.load_and_exec_sql(path, 1000)
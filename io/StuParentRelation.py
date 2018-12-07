#!/usr/bin/python
#-*-coding:utf-8-*-

import pymysql
import csv

class StuParentReloas:
    __conn = None
    __cursor = None
    schools = None
    clazz = None

    def __init__(self):
        self.get_db_conn()

    def get_db_conn(self):
        conn = pymysql.connect(host='127.0.0.1',port = 13306, user='eclass_test', passwd='test@Zuoyetong*2015', db='eclass_test', charset='utf8')
        cursor = conn.cursor()
        self.__conn = conn
        self.__cursor = cursor

    def do_load_student(self):
        print('Starting do_load_student')
        cursor = self.__cursor
        stu_sql = '''
                    SELECT t.ECLASS_USER_ID, t.ECLASS_USER_USERID FROM eclass_user t 
                    where ECLASS_USER_PARTNER_CODE=13 and t.ECLASS_USER_ROLEID = 2
                '''
        ids = dict()
        try:
            list = []

            cursor.execute(stu_sql)
            results = cursor.fetchall()
            print('查询学生完毕！，Size：%d ' % len(results))

            for row in results:
                # ids[row[0]] = row[1]
                line = str(row[0]) + ',' + str(row[1])+';'
                list.append(line)
                # self.write_txt_file('E:\Work\Talkweb\Doc\rt\stu_ids_2.txt', line)

            self.__cursor.close()

            self.write_txt_file('D:\Data\stu_ids_2.txt',list)
        except Exception as e:
            print("Error: " % e)

        return ids

    def do_load_parent(self):
        print('Starting do_load_parent')
        cursor = self.__cursor
        par_sql = '''
                    SELECT t.ECLASS_USER_ID, t.ECLASS_USER_SCHOOLNAME FROM eclass_user t 
                    where ECLASS_USER_PARTNER_CODE=13 and t.ECLASS_USER_ROLEID = 5
                '''
        ids = dict()
        try:
            list = []
            cursor.execute(par_sql)
            results = cursor.fetchall()
            print('查询家长完毕！，Size：%d ' % len(results))

            for row in results:
                # ids[row[0]] = row[1]
                line = row[0] + ',' + row[1] + ';'
                list.append(line)

            self.__cursor.close()
            print list
            self.write_txt_file('E:\\Work\\Talkweb\\Doc\\rt\\parent_ids_2.txt', list)

            title = ['stu_id', 'user_id']
            # self.write_csv('E:\\Work\\Talkweb\\Doc\tr\\parent_ids.txt',title,ids)
        except Exception as e:
            print("Error: " % e)

        return ids

    # 维护学生和家长关系
    def save_stu_parent_relation(self):
        cursor = self.__cursor
        if cursor == None:
            cursor = self.__conn.cursor()

        par_sql = '''
            SELECT t.ECLASS_USER_ID, t.ECLASS_USER_SCHOOLNAME FROM eclass_user t 
            where ECLASS_USER_PARTNER_CODE=13 and t.ECLASS_USER_ROLEID = 5
        '''

        stu_sql = '''
            SELECT t.ECLASS_USER_ID, t.ECLASS_USER_USERID FROM eclass_user t 
            where ECLASS_USER_PARTNER_CODE=13 and t.ECLASS_USER_ROLEID = 2
        '''

        par_dict = dict()
        stu_dict = dict()

        list = []
        try:
            cursor.execute(par_sql)
            results = cursor.fetchall()

            for row in results:
                par_dict[row[1]] = row[0]

            print('查询家长完毕！，Size：%d' % len(results))

            cursor.execute(stu_sql)
            results = cursor.fetchall()

            for row in results:
                stu_dict[row[1]] = row[0]

            print('查询学生完毕！，Size：%d ' % len(results))

            self.__cursor.close()

            print('读csv文件')
            url = 'E:\\Work\\Talkweb\\Doc\tr\\rel_student_parent_view.csv'
            self.read_csv(url, par_dict, stu_dict)

            print('处理完成！')
        except Exception as e:
            print("Error: " % e)

        return list

    def write_txt_file(self,path,content):
        print('Starting write_txt_file')
        try:
            with open(path, 'wb') as file:
                file.write(str(content))

            print('文件处理完成!: %s' % path)
        except Exception as e:
            print(e)

    # 读取学生-家长关系数据
    def read_csv(self, path, par_dict, stu_dict):
        list = []
        with open(path, 'rb') as file:
            csv_file = csv.reader(file)

            for i in csv_file:
                if csv_file.line_num == 1:
                    continue

                stu_id = i[0]
                par_id = i[2]
                print('stu_id: %s' % stu_id)
                print('par_id: %s' % par_id)

                if par_dict.__contains__(par_dict) and stu_dict.__contains__(stu_id):
                    sql = 'INSERT INTO eclass_parent(ECLASS_PARENT_PARENTID,ECLASS_PARENT_CHILDID) values (' + str(
                        par_dict.get(par_id)) + ',' + str(stu_dict.get(stu_id)) + ');'
                    list.append(sql)

                if csv_file.line_num == 10:
                    break

        self.write_txt_file('d:\data\rel_student_parent_view.txt',list)


if __name__ == '__main__':
    obj = StuParentReloas()
    res = obj.save_stu_parent_relation()
    # path = 'd:\\test.txt'
    # obj.write_txt_file(path,'bbcc')
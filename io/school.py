#!/usr/bin/python
# -*-coding:utf-8-*-
import csv
import sys
import time
import json

import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')


class SchoolHandler:
    def __init__(self):
        self.__conn = MySQLdb.connect(host='127.0.0.1', user='yuncl', passwd='yuncl@Zuoyetong_2014',
                                      db='yuncelian', port=13306, charset='utf8')  # 打开数据库连接
        self.__cursor = self.__conn.cursor()  # 使用cursor()方法获取操作游标

        self.grades = {"一年级": 1, "二年级": 2, "三年级": 3, "四年级": 4, "五年级": 5, "六年级": 6,
                       "七年级": 7, "八年级": 8, "九年级": 9,
                       "初一": 7, "初二": 8, "初三": 9,
                       "高一": 10, "高二": 11, "高三": 12}
        self.course_d = {14: 1, 24: 2, 34: 3, 10: 4, 20: 5, 30: 6, 16: 7, 26: 8, 36: 9, 21: 10, 31: 11, 22: 12, 32: 13,
                       23: 20, 33: 21, 25: 22, 35: 23, 27: 24, 37: 25, 28: 26, 38: 27}

        self.subject_d = {'数学': 0, '物理': 1, '化学': 2, '生物': 3, '语文': 4, '地理': 5, '英语': 6, '政治': 7, '历史': 8}

    def test(self):
        cursor = self.__cursor
        sql = " select * from eclass_school where ECLASS_SCHOOL_PARTNER_CODE = '13' limit 100"
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            print row

        cursor.close()
        self.__conn.close()

    def insert_parent(self):
        path = 'E:\\Docs\\DB\\tr\\parent_view.csv'

        sql = "insert into eclass_user(ECLASS_USER_USERNICKNAME,ECLASS_USER_PHONENUMBER,ECLASS_USER_USERID,ECLASS_USER_KEYPADID,ECLASS_USER_PARTNER_CODE,ECLASS_USER_ROLEID) values "
        vals = ""
        counter = 0

        with open(path, 'rb') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if csv_file.line_num <= 1:
                    continue

                if len(vals) == 0:
                    vals = "('" + row[2] + "','" + str(row[6]) + "','" + row[0] + "','" + row[1] + "',13,5)"
                else:
                    vals += "," + "('" + row[2] + "','" + str(row[6]) + "','" + row[0] + "','" + row[1] + "',13,5)"

                if csv_file.line_num % 10000 == 0:
                    counter += 1
                    sql_ = sql + vals + ";"
                    fname = 'parent/insert_parent_%d.sql' % counter
                    self.writeFile(fname, sql_)
                    vals = ""

            if len(vals) > 0:
                counter += 1
                sql_ = sql + vals + ";"
                fname = 'parent/insert_parent_%d.sql' % counter
                self.writeFile(fname, sql_)


    def relation_school_class(self):
        path = 'E:\\Docs\\DB\\tr\\class_view.csv'
        class_d = self.load_school()

        with open(path, 'rb') as file:
            csv_file = csv.reader(file)

            sql = "insert into eclass_schoolclass(ECLASS_SCHOOLCLASS_NAME,ECLASS_SCHOOLCLASS_BASEID,ECLASS_SCHOOLCLASS_GRADENO,ECLASS_SCHOOLCLASS_STAGE,ECLASS_SCHOOLCLASS_MASTERID,ECLASS_SCHOOLCLASS_PARTNER_CODE,ECLASS_SCHOOLCLASS_SCHOOLID,ECLASS_SCHOOLCLASS_PARTNER_CLASSID) values"
            vals = ""  # (100, 'Name 1', 'Value 1', 'Other 1'),

            for row in csv_file:
                if csv_file.line_num <= 1:
                    continue

                # print row
                if 'classId' == row[0]:
                    continue

                # print row[0], str(row[1]), row[3], row[4], row[10], row[11]

                if '幼儿园' == row[10] or len(row[10]) == 0:
                    continue

                stage = 0
                # 维护学段
                if row[10]:
                    if '九年' in row[10]:
                        if len(row[11]) == 0:
                            continue
                        else:
                            stage = self.get_stage(row[11])
                    elif '完全中学' == row[10]:
                        if len(row[11]) == 0:
                            continue
                        stage = self.get_stage(row[11])
                    else:
                        stage = self.get_stage(row[10])
                # print '学段：%d' % stage

                grade_name = str(row[1])
                # print '年级名称：%s' % grade_name

                grade = 0
                # 维护年级 初中一年级一班
                if "一年级" in grade_name and "初中一年级" not in grade_name:
                    grade = 1
                elif "二年级" in grade_name:
                    grade = 2
                elif "三年级" in grade_name:
                    grade = 3
                elif "四年级" in grade_name:
                    grade = 4
                elif "五年级" in grade_name:
                    grade = 5
                elif "六年级" in grade_name:
                    grade = 6
                elif "七年级" in grade_name or "初一" in grade_name:
                    grade = 7
                elif "八年级" in grade_name or "初二" in grade_name:
                    grade = 8
                elif "九年级" in grade_name or "初三" in grade_name:
                    grade = 9
                elif "高一" in grade_name:
                    grade = 10
                elif "高二" in grade_name:
                    grade = 11
                elif "高三" in grade_name:
                    grade = 12
                else:

                    # # 将其转换为时间数组
                    tmp_date = row[4]
                    tmp_grade = 0
                    list_date = tmp_date.split("/")
                    # print list_date

                    if len(list_date) > 1:
                        for itm in list_date:
                            print itm
                            if int(itm) > 2000:
                                if int(itm) == 2018:
                                    tmp_grade = 1
                                else:
                                    tmp_grade = 2018 - int(itm)

                        if tmp_grade > 0:
                            if stage == 2:
                                if tmp_grade == 1:
                                    grade = 7
                                elif tmp_date == 2:
                                    grade = 8
                                elif tmp_date == 3:
                                    grade = 9
                            if stage == 3:
                                if tmp_grade == 1:
                                    grade = 10
                                elif tmp_date == 2:
                                    grade = 11
                                elif tmp_date == 3:
                                    grade = 12
                            if stage == 1:
                                grade = tmp_grade

                # print '年级：%d' % grade
                if len(vals) == 0:
                    vals = " ('" + row[1] + "','" + row[2] + "'," + str(grade) + "," + str(stage) + ",'" + row[
                        6] + "',13," + str(class_d[row[2]]) + ",'" + row[0] + "')"
                else:
                    vals += "," + " ('" + row[1] + "','" + row[2] + "'," + str(grade) + "," + str(stage) + ",'" + row[
                        6] + "',13," + str(class_d[row[2]]) + ",'" + row[0] + "')"
        # print vals
        self.writeFile('update_school.sql', sql + vals)

    def relation_teacher(self):
        school_d = self.load_school()

        path = 'E:\\Docs\\DB\\tr\\teacher_view.csv'
        class_d = self.load_school()
        # ECLASS_USER_USERNAME
        sql = "insert into eclass_user(ECLASS_USER_USERNICKNAME,ECLASS_USER_SCHOOLID,ECLASS_USER_PHONENUMBER,ECLASS_USER_USERID,ECLASS_USER_KEYPADID,ECLASS_USER_PARTNER_CODE,ECLASS_USER_ROLEID) values "
        vals = ""

        with open(path, 'rb') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if csv_file.line_num <= 1:
                    continue

                # print row[0], str(row[1]), row[2], row[6], row[7], row[11]
                if len(vals) == 0:
                    vals = " ('" + row[2] + "'," + str(school_d[row[11]]) + ",'" + str(
                        row[6]) + "','" + row[0] + "','" + row[1] + "',13,3)"
                else:
                    vals += "," + " ('" + row[2] + "'," + str(school_d[row[11]]) + ",'" + str(
                        row[6]) + "','" + row[0] + "','" + row[1] + "',13,3)"

                # if csv_file.line_num > 100:
                #     break
        sql_ = sql + vals + ";\n"
        self.writeFile('insert_teacher2.sql', sql_)

    # 插入学生
    def insert_student(self):
        class_d = self.load_class2()

        path = 'E:\\Docs\\DB\\tr\\student_view2.csv'
        sql = "insert into eclass_user(ECLASS_USER_USERNICKNAME,ECLASS_USER_USERID,ECLASS_USER_KEYPADID,ECLASS_USER_PARTNER_CODE,ECLASS_USER_ROLEID,ECLASS_USER_CLASSID) values "
        vals = ""
        counter = 1
        with open(path, 'rb') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if csv_file.line_num <= 1:
                    continue

                # print row[0], row[1], row[2], row[4], row[6]

                if class_d.get(row[6]):
                    classId = class_d[row[6]]

                    if len(vals) == 0:
                        vals = "('" + row[2] + "','" + row[0] + "','" + row[1] + "',13,2,"+classId+")"
                    else:
                        vals += "," + "('" + row[2] + "','" + row[0] + "','" + row[1] + "',13,2,"+classId+")"

                # if csv_file.line_num > 100:
                #     print vals
                #     break

                if csv_file.line_num % 10000 == 0:
                    counter += 1
                    sql_ = sql + vals + ";"
                    fname = 'student/insert_student_%d.sql' % counter
                    self.writeFile(fname, sql_)
                    vals = ""

            if len(vals) > 0:
                counter += 1
                sql_ = sql + vals + ";"
                fname = 'student/insert_student_%d.sql' % counter
                self.writeFile(fname, sql_)

    def relation_student_parent(self):
        parent_d = self.load_parent()
        student_d = self.load_student()

        path = 'E:\\Docs\\DB\\tr\\rel_student_parent_view.csv'
        sql = "insert into eclass_parent(ECLASS_PARENT_CHILDID,ECLASS_PARENT_PARENTID) values "
        vals = ""
        counter=0
        with open(path, 'rb') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if csv_file.line_num <= 1:
                    continue

                # print row[0], row[1], row[2]
                parentId = parent_d.get(row[2])
                studentId = student_d.get(row[0])

                if parentId is None or studentId is None:
                    continue

                if len(vals) == 0:
                    vals = "(" + str(studentId) + "," + str(parentId) + ")"
                else:
                    vals += "," + "(" + str(studentId) + "," + str(parentId) + ")"

                if csv_file.line_num % 10000 == 0:
                    counter += 1
                    sql_ = sql + vals + ";"
                    fname = 'stu_par/insert_stu_par_%d.sql' % counter
                    self.writeFile(fname, sql_)
                    vals = ""

            if len(vals) > 0:
                counter += 1
                sql_ = sql + vals + ";"
                fname = 'stu_par/insert_stu_par_%d.sql' % counter
                self.writeFile(fname, sql_)

    # 教师教学关系
    def relation_teacher_teaching(self):
        class_d = self.load_class()
        subject_d = self.load_subject()
        teacher_d = self.load_teacher()

        path = 'E:\\Docs\\DB\\tr\\rel_teacher_class_view.csv'

        sql = "insert into eclass_teaching(ECLASS_TEACHING_TEACHERID,ECLASS_TEACHING_SUBJECTID,ECLASS_TEACHING_CLASSID,ECLASS_TEACHING_COURSE) VALUES "
        vals = ""
        vals2 = ""
        course_d = dict()
        counter = 0
        with open(path, 'rb') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if csv_file.line_num <= 1:
                    continue

                # accountId   classId
                print row[0], str(row[1]), row[3]
                accountId = str(row[0])
                classId = str(row[1])
                course_name = str(row[3])
                print course_name
                if course_name is None:
                    continue

                if self.subject_d.get(course_name) is None:
                    continue

                if class_d.get(classId):
                    class_data = class_d.get(classId).split(",")
                    stage = class_data[1]
                    class_id = class_data[0]

                    subj_code = str(stage)+''+str(self.subject_d.get(course_name))
                    if subject_d.get(subj_code):
                        subject_id = subject_d.get(subj_code)

                        user_id = teacher_d.get(accountId)

                        print class_id, subject_id, user_id

                        subjcode = str(subj_code)[1]
                        if len(vals) == 0:
                            # vals = "(" + str(user_id) + "," + str(subject_id) + "," + str(class_id) + "," + str(subj_code) + ")"
                            vals2 = "(" + str(user_id) + "," + str(0) + "," + str(0) + ",[\"" + subjcode[1] + "\"])"
                        else:
                            # vals += "," + "(" + str(user_id) + "," + str(subject_id) + "," + str(class_id) + "," + str(subj_code) + ")"
                            vals2 += "," + "(" + str(user_id) + "," + str(0) + "," + str(0) + ",[\"" + subjcode[1] + "\"])"

                        # if course_d.get(accountId) is None:
                        #     course_d[course_d] = str(subj_code)
                        # else:
                        #     course_d[course_d] = course_d[course_d] + ", " + str(subj_code)



            self.writeFile('insert_teaching.sql', sql+vals)
            self.writeFile('insert_teaching2.sql', sql+vals2)


    def relation_teaching(self):
        teaching_d = self.load_teaching()
        # print teaching_d

        sql = """
            select t.ECLASS_TEST_CLASS_TEACHERID,t.ECLASS_TEST_CLASS_CLASSID,t.ECLASS_TEST_CLASS_SUBJECTCODE ,s.ECLASS_SUBJECT_ID
            from eclass_test_class t 
            inner join  eclass_subject s on s.ECLASS_SUBJECT_CODE = t.ECLASS_TEST_CLASS_SUBJECTCODE
            group by t.ECLASS_TEST_CLASS_TEACHERID, t.ECLASS_TEST_CLASS_CLASSID;
        """

        # 从练习中维护老师和教学关系
        sql = """
            select t.ECLASS_EXERCISE_OWNERID,t.ECLASS_EXERCISE_CLASSID,t.ECLASS_EXERCISE_SUBJECTID,s.ECLASS_SUBJECT_CODE 
            from eclass_exercise t 
            inner join eclass_subject s on s.ECLASS_SUBJECT_ID = t.ECLASS_EXERCISE_SUBJECTID
            inner join eclass_user u on u.ECLASS_USER_ID = t.ECLASS_EXERCISE_OWNERID
            where ECLASS_EXERCISE_CLASSID is not null
            GROUP BY ECLASS_EXERCISE_OWNERID,ECLASS_EXERCISE_CLASSID,ECLASS_EXERCISE_SUBJECTID
        """

        insert_sql = "insert into eclass_teaching(ECLASS_TEACHING_TEACHERID,ECLASS_TEACHING_SUBJECTID,ECLASS_TEACHING_CLASSID,ECLASS_TEACHING_COURSE) values "
        vals = ""
        self.__cursor.execute(sql)
        res = self.__cursor.fetchall()
        for row in res:
            key = str(row[0]) + '-' + str(row[1]) + '-' + str(row[2])
            if teaching_d.get(key):
                continue

            if len(vals) == 0:
                vals = "(" + str(row[0]) + "," + str(row[2]) + "," + str(row[1]) + "," + str(row[3]) + ")"
            else:
                vals += "," + "(" + str(row[0]) + "," + str(row[2]) + "," + str(row[1]) + "," + str(row[3]) + ")"

        self.writeFile('insert_teaching_relation2.sql', insert_sql + vals)


    def relation_teaching_init(self):
        sql = """
            select t.ECLASS_TEACHING_TEACHERID,t.ECLASS_TEACHING_CLASSID,(ECLASS_TEACHING_COURSE)
            from eclass_teaching t where  t.ECLASS_TEACHING_CLASSID<>0 and t.ECLASS_TEACHING_COURSE is not null and  
             t.ECLASS_TEACHING_TEACHERID in (
                select distinct ECLASS_EXERCISE_OWNERID from (
                select t.ECLASS_EXERCISE_OWNERID,t.ECLASS_EXERCISE_CLASSID,t.ECLASS_EXERCISE_SUBJECTID,s.ECLASS_SUBJECT_CODE 
                from eclass_exercise t 
                inner join eclass_subject s on s.ECLASS_SUBJECT_ID = t.ECLASS_EXERCISE_SUBJECTID
                inner join eclass_user u on u.ECLASS_USER_ID = t.ECLASS_EXERCISE_OWNERID
                where ECLASS_EXERCISE_CLASSID is not null
                GROUP BY ECLASS_EXERCISE_OWNERID,ECLASS_EXERCISE_CLASSID,ECLASS_EXERCISE_SUBJECTID
                )a)
        """

        tea_course = dict()
        self.__cursor.execute(sql)
        res = self.__cursor.fetchall()
        for row in res:
            # print row[0], row[1], row[2]
            teacherid = row[0]
            sub_code = row[2]

            if len(sub_code)>0 and sub_code.find("]")>0:
                sub_code = json.loads(sub_code)[0]
            if len(sub_code) == 2:
                tmp_code = sub_code[1]
            else:
                tmp_code = sub_code

            if tea_course.get(teacherid):
                val = tea_course.get(teacherid)
                if tmp_code in val:
                    continue
                else:
                    tea_course[teacherid] = tea_course[teacherid]+","+tmp_code
            else:
                tea_course[teacherid] = tmp_code

        # print tea_course
        vals = ""
        delete_sql = "delete from eclass_teaching where ECLASS_TEACHING_CLASSID = 0 and  ECLASS_TEACHING_TEACHERID in "
        list_teacherids = []
        insert_sql = "insert into eclass_teaching(ECLASS_TEACHING_TEACHERID,ECLASS_TEACHING_SUBJECTID,ECLASS_TEACHING_CLASSID,ECLASS_TEACHING_COURSE,ECLASS_TEACHING_ISPASS) values "
        for row in res:
            if tea_course.get(row[0]):
                if row[0] in list_teacherids:
                    continue
                else:
                    list_teacherids.append((row[0]))

                codes = tea_course.get(row[0])
                tmp_cour_code = ""
                # print codes
                for itm in codes.split(","):
                    if len(tmp_cour_code) == 0:
                        tmp_cour_code = "[\""+itm+"\""
                    else:
                        tmp_cour_code += ",\""+itm+"\""
                tmp_cour_code += "]"
                if len(vals) == 0:
                    vals = "(" + str(row[0]) + ",0,0,'" + tmp_cour_code + "',9)"
                else:
                    vals += "," + "(" + str(row[0]) + ",0,0,'" + tmp_cour_code + "',9)"
        self.writeFile('insert_teaching_init2.sql', insert_sql + vals)

        ids = ""
        print list_teacherids
        for i in list_teacherids:
           ids += ""+str(i)+","
        print ids
        self.writeFile("delete_teaching_init2.sql", delete_sql+"("+ids+")")

    def update_teacher(self):
        sql = """select ECLASS_TEACHING_TEACHERID, ECLASS_TEACHING_CLASSID  from eclass_teaching t
                 inner join eclass_user u on u.ECLASS_USER_ID = t.ECLASS_TEACHING_TEACHERID
                 where  u.ECLASS_USER_PARTNER_CODE=13 and u.ECLASS_USER_ROLEID=3 and t.ECLASS_TEACHING_CLASSID<>0
                """

        self.__cursor.execute(sql)
        res = self.__cursor.fetchall()
        teacher_class_d = dict()

        for row in res:
            # print row[0], row[1]
            sql = "update eclass_user set  ECLASS_USER_CLASSID= %d where  ECLASS_USER_ID= %d ;\n" % (row[1], row[0])
            # print sql
            self.writeFile("update_teacher_classid.sql", sql)

        self.__cursor.close()
        self.__conn.close()
        print 'finishi'

    def update_student_school(self):
        class_d = self.load_class_school()

        sql = """select u.ECLASS_USER_ID,u.ECLASS_USER_CLASSID 
                 from eclass_user u where u.ECLASS_USER_PARTNER_CODE=13 and u.ECLASS_USER_ROLEID=2 and ECLASS_USER_SCHOOLID is null
                """

        self.__cursor.execute(sql)
        res = self.__cursor.fetchall()

        counter = 0
        update_sql = ""
        num=0
        for row in res:
            num+=1
            # print row[0], row[1]
            if class_d.get(row[1]):
                schoolId = int(class_d.get(row[1]))
                update_sql += "update eclass_user set  ECLASS_USER_SCHOOLID= %d where  ECLASS_USER_ID= %d ;\n" % (schoolId, row[0])
                # try:
                #     self.__cursor.execute(update_sql)
                #     self.__conn.commit()
                # except Exception as e:
                #     self.conn.rollback()
                #     print("执行SQL时出错：%s" % (e))

                if num % 1000 == 0:
                    counter += 1
                    # fname = 'update_student/update_student_shoolid_%d.sql' % counter
                    # self.writeFile(fname, update_sql)
                    try:
                        self.__cursor.executemany(update_sql)
                        self.__conn.commit()
                    except Exception as e:
                        self.conn.rollback()
                        print("执行SQL时出错：%s" % (e))
                    update_sql = ""

        if len(update_sql) > 0:
            counter += 1
            # fname = 'update_student/update_student_shoolid_%d.sql' % counter
            # self.writeFile(fname, update_sql)
            try:
                self.__cursor.executemany(update_sql)
                self.__conn.commit()
            except Exception as e:
                self.conn.rollback()
                print("执行SQL时出错：%s" % (e))


        self.__cursor.close()
        self.__conn.close()
        print 'finishi'


    def update_student_school2(self):
        class_d = self.load_class_school()

        sql = """select u.ECLASS_USER_ID,u.ECLASS_USER_CLASSID 
                 from eclass_user u where u.ECLASS_USER_PARTNER_CODE=13 and u.ECLASS_USER_ROLEID=2 and ECLASS_USER_SCHOOLID is null
                """

        self.__cursor.execute(sql)
        res = self.__cursor.fetchmany(1000)

        counter = 0
        update_sql = ""
        num=0
        for row in res:
            num+=1
            # print row[0], row[1]
            if class_d.get(row[1]):
                schoolId = int(class_d.get(row[1]))
                update_sql += "update eclass_user set  ECLASS_USER_SCHOOLID= %d where  ECLASS_USER_ID= %d ;\n" % (schoolId, row[0])
                # try:
                #     self.__cursor.execute(update_sql)
                #     self.__conn.commit()
                # except Exception as e:
                #     self.conn.rollback()
                #     print("执行SQL时出错：%s" % (e))

                if num % 1000 == 0:
                    counter += 1
                    # fname = 'update_student/update_student_shoolid_%d.sql' % counter
                    # self.writeFile(fname, update_sql)
                    try:
                        self.__cursor.executemany(update_sql)
                        self.__conn.commit()
                    except Exception as e:
                        self.conn.rollback()
                        print("执行SQL时出错：%s" % (e))
                    update_sql = ""

        if len(update_sql) > 0:
            counter += 1
            # fname = 'update_student/update_student_shoolid_%d.sql' % counter
            # self.writeFile(fname, update_sql)
            try:
                self.__cursor.executemany(update_sql)
                self.__conn.commit()
            except Exception as e:
                self.conn.rollback()
                print("执行SQL时出错：%s" % (e))


        self.__cursor.close()
        self.__conn.close()
        print 'finishi'

    def load_school(self):
        cursor = self.__cursor
        sql = "select t.ECLASS_SCHOOL_ID,t.ECLASS_SCHOOL_PARTNER_SCHOOLID from eclass_school t where t.ECLASS_SCHOOL_PARTNER_CODE=13 "
        cursor.execute(sql)
        res = cursor.fetchall()
        class_d = dict()

        for row in res:
            class_d[row[1]] = row[0]
        return class_d

    def load_class(self):
        cursor = self.__cursor
        sql = "select t.ECLASS_SCHOOLCLASS_ID,t.ECLASS_SCHOOLCLASS_PARTNER_CLASSID,ECLASS_SCHOOLCLASS_STAGE from eclass_schoolclass t where t.ECLASS_SCHOOLCLASS_PARTNER_CODE=13 "
        cursor.execute(sql)
        res = cursor.fetchall()
        class_d = dict()

        for row in res:
            class_d[row[1]] = str(row[0]) + "," + str(row[2])
        return class_d

    def load_class2(self):
        cursor = self.__cursor
        sql = "select t.ECLASS_SCHOOLCLASS_ID,t.ECLASS_SCHOOLCLASS_PARTNER_CLASSID from eclass_schoolclass t where t.ECLASS_SCHOOLCLASS_PARTNER_CODE=13 "
        cursor.execute(sql)
        res = cursor.fetchall()
        class_d = dict()

        for row in res:
            class_d[row[1]] = str(row[0])
        return class_d

    def load_class_school(self):
        cursor = self.__cursor
        sql = "select ECLASS_SCHOOLCLASS_ID,t.ECLASS_SCHOOLCLASS_SCHOOLID from eclass_schoolclass t where t.ECLASS_SCHOOLCLASS_PARTNER_CODE=13 "
        cursor.execute(sql)
        res = cursor.fetchall()
        class_school_d = dict()
        for row in res:
            class_school_d[row[0]] = row[1]
        return class_school_d


    def load_subject(self):
        cursor = self.__cursor
        sql = "select t.ECLASS_SUBJECT_ID,t.ECLASS_SUBJECT_CODE from eclass_subject t "
        cursor.execute(sql)
        res = cursor.fetchall()
        subjct_d = dict()

        for row in res:
            subjct_d[row[1]] = row[0]
        return subjct_d

    def load_teacher(self):
        cursor = self.__cursor
        sql = "select t.ECLASS_USER_ID,t.ECLASS_USER_KEYPADID from eclass_user t "
        cursor.execute(sql)
        res = cursor.fetchall()
        tea_d = dict()
        for row in res:
            tea_d[row[1]] = row[0]
        return tea_d

    def load_parent(self):
        cursor = self.__cursor
        sql = "select t.ECLASS_USER_ID,t.ECLASS_USER_KEYPADID from eclass_user t where ECLASS_USER_ROLEID=5 and t.ECLASS_USER_PARTNER_CODE=13 "
        cursor.execute(sql)
        res = cursor.fetchall()
        tea_d = dict()
        for row in res:
            tea_d[row[1]] = row[0]
        return tea_d

    def load_student(self):
        cursor = self.__cursor
        sql = "select t.ECLASS_USER_ID,t.ECLASS_USER_USERID from eclass_user t where ECLASS_USER_ROLEID=2 and t.ECLASS_USER_PARTNER_CODE=13 "
        cursor.execute(sql)
        res = cursor.fetchall()
        tea_d = dict()
        for row in res:
            tea_d[row[1]] = row[0]
        return tea_d

    def load_teaching(self):
        cursor = self.__cursor
        sql = """ select t.ECLASS_TEACHING_TEACHERID,t.ECLASS_TEACHING_CLASSID,t.ECLASS_TEACHING_COURSE from eclass_teaching t 
                   where ECLASS_TEACHING_CLASSID = 0 and ECLASS_TEACHING_TEACHERID in (
                        select distinct ECLASS_TEST_CLASS_TEACHERID
                        from eclass_test_class 
                        group by ECLASS_TEST_CLASS_TEACHERID, ECLASS_TEST_CLASS_CLASSID
        ) """
        cursor.execute(sql)
        res = cursor.fetchall()
        teaching_d = dict()
        for row in res:
            course = str(row[2]).replace("[","").replace("]","").replace("\"","")
            key = str(row[0])+'-'+str(row[1])+'-'+course
            teaching_d[key] = row[0]
        return teaching_d

    def update_class_schooldid(self):
        cursor = self.__cursor
        sql = "select * from tmp_class_school"
        cursor.execute(sql)
        res = cursor.fetchall()
        class_d = dict()
        for row in res:
            class_d[row[0]] = row[1]
        sql = "select ECLASS_SCHOOLCLASS_ID from eclass_schoolclass t where t.ECLASS_SCHOOLCLASS_PARTNER_CODE='13' "
        cursor.execute(sql)
        c_res = cursor.fetchall()
        for row in c_res:
            # print row[0]
            class_id = row[0]
            # print type(class_d)
            if class_d.get(class_id):
                tmp_sql = "update eclass_schoolclass set ECLASS_SCHOOLCLASS_ID= %d where ECLASS_SCHOOLCLASS_ID=%d ;\n" % (
                    class_d[class_id], class_id)
                self.writeFile('update_class_schoolid.sql', tmp_sql)


    def get_stage(self, name):
        stage = 0
        if '小' in name:
            stage = 1
        elif '初' in name:
            stage = 2
        elif '高' in name:
            stage = 3
        return stage

    def read_csv_file(self, path):
        with open(path, 'rb') as file:
            csv_file = csv.DictReader(file)
            return csv_file

    def writeFile(self, path, content):
        with open(path, 'a') as f:
            f.write(content)


if __name__ == '__main__':
    obj = SchoolHandler()
    # obj.relation_teacher_teaching()
    # obj.insert_parent()
    # obj.insert_student()
    # obj.update_teacher()
    # obj.update_student_school()
    # obj.relation_teaching()
    obj.relation_teaching_init()
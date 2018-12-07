#!/usr/bin/python
#-*-coding:utf-8-*-
import json

import psycopg2


def conn():
    conn = psycopg2.connect(database="ycl_resource", user="root", password="pangu", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    sql = 'SELECT t.sections, t.points FROM t_ques t where t.qid=\'43d41291-41ac-589e-b4db-08ae913a5baf\''
    print sql
    cur.execute(sql)
    rows = cur.fetchall()

    list = []

    for row in rows:
        print row[0], row[1]
        sections = json.dumps(row[0], ensure_ascii=False)
        print type(row[0])
        for item in row[0]:
            print item['code'], item['name']
            list.append(str(item['code']))

    print list

conn()
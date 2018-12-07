#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def read_file(path):
    list1  = []
    with open(path, 'r') as f:
        for line in f.readlines():
            # print line
            list1.append(line)
        return list1

def writeFile(path,content):
    with open(path, 'a') as f:
        f.write(content)

def compare_file():
    file1 = 'censor2.txt'
    file2 = 'new-consor.txt'

    list = read_file(file1)
    list1 = read_file(file2)
    print len(list)
    print len(list1)
    # for row in list
    for row in list1:
        if not row in list:
            print row
            writeFile('test.txt', row)




compare_file()
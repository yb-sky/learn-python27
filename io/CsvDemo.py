#!/usr/bin/python
#-*-coding:utf-8-*-

import csv
import codecs

class HandlerCsv:

    def read_csv(self,path):
        print(path)
        with open(path, 'rb') as file:
            csv_file = csv.reader(file)

            for i in csv_file:
                # print('steName:%s,step:%s,name:%s',str(i[10]),str(i[11]),str(i[1]))
                print(i[1])
                print(i[2])
                if csv_file.line_num == 10:
                    break

    def write_csv(self,path):
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["index", "a_name", "b_name"])
            list = []
            list.append([0, 1, 3])
            list.append([1, 2, 3])
            list.append([2, 3, 4])

            # 写入多行用writerows
            # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])
            writer.writerows(list)

            file.close()


    def read_csv_file(self,path):
        with open(path, 'r') as file:
            csv_file = csv.reader(file)
            print(csv_file)
            for row in csv_file:
                print row[0], row[1], row[2]
            file.close()

    def test_write(self):
        writer = csv.writer(file('test1.csv', 'wb'))
        writer.writerow(['Column1', 'Column2', 'Column3'])
        lines = [range(3) for i in range(5)]
        for line in lines:
            writer.writerow(line)

if __name__ == '__main__':
    obj = HandlerCsv()
    # obj.read_csv('E:\\Docs\\DB\\tr\\school_view.csv')

    dd = dict()
    dd[1]=2
    print dd.get(2)

    # obj.write_csv('test1.csv')

    # obj.test_write()
    # obj.read_csv_file('E:\\Work\\Talkweb\\Doc\tr\\rel_student_parent_view.csv')





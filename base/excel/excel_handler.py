#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import datetime
import xlrd

# from collections import namedtuple
import utils.fileUtils as futil
import utils.reUtils as reutil

"""
    for：统计每个工序每天的总量和不良数
    xlrd参考：https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
"""

class handlerExcel:
    title = ['工序名称','当日产量','不良数']

    def __init__(self):
        pass

    def main(self):
        """
        1. 重命名报表文件，加载报表工序
        2. 根据1的工序统计流水的 “当日产量“和”不良数”
        3. 生成工序对应的统计报表
        4. 删除生成的临时report.xlsx
        5. 将data/所有文件移到result下
        """

        toda = datetime.date.today()

        report_path = (self.get_file_name('report'))
        salary_path = (self.get_file_name('data'))
        pro_list = self.get_production_list(report_path)
        pro_total_list = self.get_day_production_total(pro_list, salary_path)

        day_report_file = 'result/report-'+str(toda)+'.xlsx'
        self.write_excel(day_report_file, pro_list, pro_total_list)

        futil.move_file(salary_path, 'result/')
        print('程序执行结束，报表路径：%s' % day_report_file)

    # 读取excel文件内容
    def read_excel(self, fileName):
        wookbook = xlrd.open_workbook(fileName)
        table = wookbook.sheets()[0]
        return table

    def get_file_name(self, dir):
        try:
            file = os.listdir(dir)[0]
            return dir + '/' + file.decode('gbk')
        except Exception as result:
            print('data目录无文件。')
            sys.exit()


    # 将工序添加到一个list返回
    def get_production_list(self, fileName):
        print('开始处理：%s' % fileName)
        table = self.read_excel(fileName)
        rows = table.nrows
        # cols = table.ncols
        list = []
        for row in range(rows):
            if row < 3 or '总合计' == row:
                continue

            # table.row_values(rowx, start_colx=0, end_colx=None)
            production = table.row_values(row, start_colx=1, end_colx=2)
            if len(production) > 0:
                pro = reutil.remove_chinese(str(production[0]))

                if len(pro) == 0:
                    continue

                if pro in list:
                    continue

                list.append(pro)

        return list

    # 统计产品一天的总量和不良数
    def get_day_production_total(self, pro_list, fileName):
        table = self.read_excel(fileName)
        rows = table.nrows

        print('\n 开始处理工资表： ')
        pro_detail = dict()

        for row in range(rows):
            if row < 2:
                continue

            # table.row_values(rowx, start_colx=0, end_colx=None)
            production = table.row_values(row, start_colx=3, end_colx=6)
            if len(str(production[0]).strip()) == 0:
                continue

            pro = reutil.remove_chinese(str(production[0]))
            if len(pro) == 0:
                continue

            if pro in pro_list:
                total = str(production[1])
                bad_total = str(production[2])
                old_pro_detail = pro_detail.get(pro)

                if old_pro_detail:
                    total_ = float(old_pro_detail.split('&')[0])
                    if len(total) > 0:
                        total_ = total_ + float(total)

                    bad_total_ = float(old_pro_detail.split('&')[1])
                    if len(bad_total) > 0:
                        bad_total_ = bad_total_ + float(bad_total)

                    pro_detail[pro] = str(total_) + '&' + str(bad_total_)

                else:
                    if len(total) == 0:
                        total = '0'
                    if len(bad_total) == 0:
                        bad_total = '0'

                    pro_detail[pro] = str(total) + '&' + str(bad_total)

        return (pro_detail)

    def write_excel(self, fileName, pro_list, pro_total):
        import xlsxwriter

        # encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
        # style_compression:表示是否压缩，不常用
        book = xlsxwriter.Workbook(fileName)
        sheet = book.add_worksheet('report')
        top = book.add_format(
            {'border': 1, 'align': 'center', 'bg_color': 'cccccc', 'font_size': 13, 'bold': True})  # 设置单元格格式

        sheet.write_row('A1', self.title)
        # for i in range(0, len(self.title)):
        #     sheet.write(0, i, self.title[i])

        for row in range(len(pro_list)):
            pro = pro_list[row]
            # print(pro)
            pro_detail = pro_total.get(pro)
            if pro_detail:
                # print(pro_detail.split('&'))
                sheet.write_row('A' + str(row), [pro, pro_detail.split('&')[0], pro_detail.split('&')[1]])
            else:
                sheet.write_row('A' + str(row), [pro, '', ''])
                pass

        book.close()

    def test(self):
        salary_path = (self.get_file_name('data'))
        futil.move_file(salary_path, 'result/')

if __name__ == '__main__':
    obj = handlerExcel()
    obj.main()
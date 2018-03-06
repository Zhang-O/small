# -*- coding:utf-8 -*-
# Filename: try.py
# Author：zhang
# Date: 2018/3/4 22:41

import xlrd, os

import xlrd

excelFile = './rg_score.xlsx'

sset = set()
snum = list()

exception_file = []

data = xlrd.open_workbook(excelFile)

table = data.sheets()[0]

nrows = table.nrows  # 行数

ncols = table.ncols  # 列数

def copy(fsrc, fdes):
    # print(src)
    # print(des)
    global exception_file
    if not os.path.exists(fsrc):
        print("{} 不存在".format(fsrc))
        exception_file.append(fsrc)
        return

    with open(fsrc, 'rb') as fr:
        with open(fdes, 'wb') as fw:
            fw.write(fr.read())


for i in range(1, nrows):
    rowValues = table.row_values(i)  # 某一行数据
    basic_path = 'D:/宁波模拟考试201801/nbky2018end0128/IMP/'
    src = basic_path + '/'.join(rowValues[2].split('/')[1:-1]) + '.zip'
    des = basic_path + 'ren_gong_ding_biao/' + str(int(rowValues[1])) + '.zip'
    copy(src, des)
    # print(rowValues)
    # for item in rowValues:
    #     print(item)

    # sset.add(int(rowValues[1]))
    # snum.append(int(rowValues[1]))

# print(len(sset))
# print(len(snum))

with open(basic_path + 'exception_file.txt', 'w') as f:
    f.write('\n'.join(exception_file))

with open("file://10.33.3.91/s5/part1/2101/210101014/141/174/16200202/B55F145740831415DE47CA5AC10E6BAD/16200203/Answer.xml", 'rb') as f:
    print(f.read())









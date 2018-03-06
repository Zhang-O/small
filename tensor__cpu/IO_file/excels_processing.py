# -*- coding:utf-8 -*-
"""todo"""

import xlwt, xlrd, xlsxwriter
import os


def pre_process(src_file):

    """-------------------------------- xlrd ------------------------------------------------"""
    data = xlrd.open_workbook(src_file, encoding_override="utf8")
    table = data.sheets()[0]

    rows = table.nrows
    cols = table.ncols

    print(rows, cols)
    # for row in range(rows):
    #     print(table.row_values(row))

    # 可以写到 table 里面， 但是无法保存
    # table.put_cell(1, 1, 1, '222', 0)
    # print(rows, cols)
    # for row in range(rows):
    #     print(table.row_values(row))


    """ ----------------------------------xlwt 设置宽高等样式不灵活 -----------------------------------------------"""
    # wbk = xlwt.Workbook(encoding='utf-8')
    # sheet = wbk.add_sheet('sheet1', cell_overwrite_ok=True)  # 第二参数用于确认同一个cell单元是否可以重设值。
    # style = xlwt.XFStyle()
    # font = xlwt.Font()
    # font.name = 'Times New Roman'
    # font.bold = True
    # style.font = font
    #
    # # sheet.write(0, 1, 'some bold Times text', style)
    #
    # for row in range(rows):
    #     for col in range(cols):
    #         sheet.write(row, col, table.cell(row, col).value)
    #
    # wbk.save('./test2.xls')  # 扩展名为 xls  不能为xlsx


    """----------------------------------xlwt -----------------------------------------------"""
    target_file = os.path.join(os.path.dirname(src_file), 're_' + os.path.basename(src_file))
    workbook = xlsxwriter.Workbook(target_file)
    worksheet = workbook.add_worksheet()

    # 设置宽度
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 40)
    worksheet.set_column('G:G', 20)

    for row in range(rows):
        for col in range(cols):
            worksheet.write(row, col, table.cell(row, col).value)
            worksheet.write_url(row, 1, table.cell(row, 3).value, string=table.cell(row, 1).value)
            # worksheet.write_formula(row, 1, '=SUM(1, 2, 3)')
            # worksheet.write_formula(row, 1, '=SUM(1, 2, 3)')
            # print('=HYPERLINK({}, {})'.format(table.cell(row, 3).value, table.cell(row, 1).value))
            # worksheet.write(row, 1, '=HYPERLINK({}, {})'.format(table.cell(row, 3).value, table.cell(row, 1).value))

    workbook.close()


# \\10.33.2.231\share\QT-742440ans.mp3

pre_process('./test.xlsx')

# -*- coding:utf-8 -*-
import xlwt,xlsxwriter

    # ws = workbook.add_worksheet(exam_name)
    # # 设置宽度
    # ws.set_column('A:A', 25)
    # ws.set_column('B:B', 25)
    # ws.set_column('C:C', 15)
    # ws.set_column('D:D', 15)
    # # 写表头
    # ws.write(0, 0, u'试卷ID')
    # ws.write(0, 1, '考生ID'.decode('utf8'))
    # ws.write(0, 2, '题号'.decode('utf8'))
    # ws.write(0, 3, '分数'.decode('utf8'))
    #
    # # get paper info
    # cursor.execute(
    #     'select paperid,studentid,itemid,itemscore from AI_Answer where examid = %s and itemstatus = %s',
    #     (examid, '99'))
    # scores_data = cursor.fetchall()
    # all_scores = []  # 这是为了在worksheet2中使用，以免再次进行sql查询，导致不一致
    # number = len(scores_data)
    # for i in range(number):
    #     ws.write(i + 1, 0, scores_data[i]['paperid'].decode('utf8'))
    #     ws.write(i + 1, 1, scores_data[i]['studentid'].decode('utf8'))
    #     ws.write(i + 1, 2, scores_data[i]['itemid'].decode('utf8'))
    #     ws.write(i + 1, 3, scores_data[i]['itemscore'])
    #     all_scores.append(scores_data[i]['itemscore'])
    #
    # # 2. -------------------------------------插入图表 ----------------------------------------
    # # workbook = xlsxwriter.Workbook(destination)
    # worksheet2 = workbook.add_worksheet(u'成绩分布图')
    # bold = workbook.add_format({'bold': 1})
    # # 这是个数据table的列
    # headings = [u'分数段', u'个数']
    #
    # data = [
    #     ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100'],
    # ]
    # frequency = []
    # for i in range(10):
    #     # 计算每个分数段的个数，不能直接用sql 查，是因为 数据库可能存在更新操作
    #     def select_condition(arg):
    #         if i == 0:
    #             if arg >= 0 and arg <= (i + 1) * 10:
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             if arg > i * 10 and arg <= (i + 1) * 10:
    #                 return True
    #             else:
    #                 return False
    #
    #
    #     frequency.append(len(list(filter(select_condition, all_scores))))
    #
    # # 写入一行
    # worksheet2.write_row('A1', headings, bold)
    # # 写入一列
    # worksheet2.write_column('A2', data[0])
    # worksheet2.write_column('B2', frequency)
    #
    # ############################################
    # # 创建一个图表，类型是column
    # chart1 = workbook.add_chart({'type': 'column'})
    # # 配置series,这个和前面worksheet是有关系的。
    # chart1.add_series({
    #     'name': [u'成绩分布图', 0, 1],
    #     'categories': [u'成绩分布图', 1, 0, 10, 0],
    #     'values': [u'成绩分布图', 1, 1, 10, 1],
    # })
    # #      添加图表标题和标签
    # chart1.set_title({'name': u'成绩分布直方图'})
    # chart1.set_x_axis({'name': u'分数段'})
    # chart1.set_y_axis({'name': u'数量'})
    # # 设置图表风格
    # chart1.set_style(11)
    # # 在D2单元格插入图表（带偏移）
    # worksheet2.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
    #
    # # 生成饼图
    # chart4 = workbook.add_chart({'type': 'pie'})
    # # 定义数据
    # chart4.add_series({
    #     'name': u'成绩分布百分比图',
    #     'categories': [u'成绩分布图', 1, 0, 10, 0],
    #     'values': [u'成绩分布图', 1, 1, 10, 1],
    #     'points': [
    #         {'fill': {'color': 'black'}},
    #         {'fill': {'color': 'white'}},
    #         {'fill': {'color': 'orange'}},
    #         {'fill': {'color': 'brown'}},
    #         {'fill': {'color': 'yellow'}},
    #         {'fill': {'color': 'purple'}},
    #         {'fill': {'color': 'blue'}},
    #         {'fill': {'color': 'red'}},
    #         {'fill': {'color': 'magenta'}},
    #         {'fill': {'color': 'green'}},
    #     ],
    # })
    # # Add a chart title and some axis labels.
    # chart4.set_title({'name': u'成绩分布百分比'})
    # chart4.set_style(3)
    #
    # worksheet2.insert_chart('D20', chart4, {'x_offset': 25, 'y_offset': 10})
    #
    # # 3. ----------------------- 新增一个worksheet 用于比较双引擎的分数 --------------------------
    # worksheet3 = workbook.add_worksheet(u'双引擎分数比较')
    # # 设置宽度
    # worksheet3.set_column('A:A', 20)
    # worksheet3.set_column('B:B', 20)
    # worksheet3.set_column('C:C', 10)
    # worksheet3.set_column('D:D', 10)
    # worksheet3.set_column('E:E', 10)
    # worksheet3.set_column('F:F', 10)
    # worksheet3.set_column('G:G', 10)
    # # 写表头
    # worksheet3.write(0, 0, u'试卷ID')
    # worksheet3.write(0, 1, u'考生ID')
    # worksheet3.write(0, 2, u'题号')
    # worksheet3.write(0, 3, u'分数1')
    # worksheet3.write(0, 4, u'分数2')
    # worksheet3.write(0, 5, u'分数差值')
    # worksheet3.write(0, 6, u'最终分数')
    #
    # # get paper info
    # format_red = workbook.add_format({'bold': True, 'font_color': 'red'})
    # # format_red.set_font_color('red')
    # format_yellow = workbook.add_format({'bold': True, 'font_color': 'green'})
    # # format.set_font_color('yellow')
    #
    # cursor.execute(
    #     'select paperid,studentid,itemid,score1,score2,itemscore from AI_Answer where examid = %s and itemstatus = %s',
    #     (examid, '99'))
    # scores_detail = cursor.fetchall()
    # _number = len(scores_detail)
    # for i in range(_number):
    #     worksheet3.write(i + 1, 0, scores_detail[i]['paperid'].decode('utf8'))
    #     worksheet3.write(i + 1, 1, scores_detail[i]['studentid'].decode('utf8'))
    #     worksheet3.write(i + 1, 2, scores_detail[i]['itemid'].decode('utf8'))
    #     worksheet3.write(i + 1, 3, scores_detail[i]['score1'])
    #     worksheet3.write(i + 1, 4, scores_detail[i]['score2'])
    #     delta = abs(scores_detail[i]['score2'] - scores_detail[i]['score1'])
    #     worksheet3.write(i + 1, 5, delta)
    #     if scores_detail[i]['score2'] == -888 or scores_detail[i]['score1'] == -888:
    #         worksheet3.write(i + 1, 6, 'XXX', format_red)  # 评分失败
    #     elif delta > 15:  # 评分误差大于15分
    #         worksheet3.write(i + 1, 6, 'OOO', format_yellow)
    #     elif delta <= 15:
    #         worksheet3.write(i + 1, 6, (scores_detail[i]['score2'] + scores_detail[i]['score1']) / 2)
    # # 关闭工作簿
    # workbook.close()
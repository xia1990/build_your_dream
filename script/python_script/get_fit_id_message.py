#!/usr/bin/python
import xlrd,xlwt

elvis_id_list=[]
data_list=[]
with open('elvis_0329.txt') as ft:
    for eid in ft:
        elvis_id_list.append(int(eid))
#    print elvis_id_list

data = xlrd.open_workbook('0329_total.xls')
table = data.sheets()[0]
for row in range(0,table.nrows):
    if not row == 0:
        temp_id=int(table.cell(row,0).value)
        if temp_id in elvis_id_list:
            #print table.row_values(row)
            print len(table.row_values(row))
            print table.row_values(row)
            data_list.append(table.row_values(row))

    else:
        data_list.append(table.row_values(row))



workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
for row in range(0,len(data_list)):
    for col in range(0,14):
        if  row == 0:
            worksheet.write(row, col, label = data_list[row][col])
        else:
            if col == 4 or col == 6 or col == 12:
                if isinstance(data_list[row][col],float):
					#读取表格中的日期格式，为元组形式
                    date_tuple=xlrd.xldate_as_tuple(data_list[row][col],0)
                    dd="%s/%s/%s" % (date_tuple[0],date_tuple[1],date_tuple[2])
                    worksheet.write(row, col, label = dd)
            else:
                worksheet.write(row, col, label = data_list[row][col])

workbook.save('Excel_Workbook.xls')

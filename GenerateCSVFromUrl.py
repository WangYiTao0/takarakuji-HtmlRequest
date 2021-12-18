import csv

import pandas as pd
#显示所有列
#pd.set_option('display.max_columns', None)
#显示所有行
#pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
#pd.set_option('max_colwidth',100)
import xlwt as xlwt


def GenerateCSV(url,filename) :
    table = pd.read_html(url)[0]
    originfilename = 'dfOrigin.csv'
    file = table.to_csv(originfilename, encoding='utf-8-sig', header=0, index=0)
    df = pd.read_csv(originfilename)
    #print(df)
    df_new = df.drop([51,153,154,155,156,157,158])
    df_new.to_csv(filename)


def remove_specific_row_from_csv(file,column_name,*args):
    '''
    :param file:file to remove the rows from
    :param column_name:The column that determines which row will be
           deleted (e.g. if Column == Name and row-*args
           contains "Gavri", All rows that contain this word will be deleted)
    :param args: Strings from the rows according to the conditions with
                 the column
    :return:
    '''
    row_to_remove = []
    for row_name in args:
        row_to_remove.append(row_name)
    try:
        df = pd.read_csv(file)
        for row in row_to_remove:
            df = df[eval("df.{}".format(column_name)) != row]
        df.to_csv(file, index=False)
    except Exception as e:
        raise Exception("Error message....")

def csv_to_xlsx(filename,excelfileName,sheetName):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(sheetName)  # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1
        workbook.save(excelfileName)  # 保存Excel

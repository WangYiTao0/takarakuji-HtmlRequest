from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Color, PatternFill

import readcsv
from GenerateCSVFromUrl import GenerateCSV, remove_specific_row_from_csv, csv_to_xlsx
from readcsv import ReadCSVFile
import openpyxl

url = 'http://www.ohtashp.com/topics/takarakuji/'
csv_file_Name = 'kuji.csv'
excel_file_Name = 'kuji.xlsx'
excel_file_temp_Name = 'kuji_temp.xlsx'

GenerateCSV(url, csv_file_Name)
ReadCSVFile(csv_file_Name)
# csv_to_xlsx(csv_file_Name,excel_file_Name,"2019-2021")

# for i in range(len(readcsv.key)):
#     print(readcsv.key[i])
#     print(kujiData[readcsv.key[i]])

# workbook
# worksheet
# row column cell
wb = openpyxl.load_workbook(excel_file_Name)

column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

row1 = ['回別', '抽選日', '本数字', 'bonus数字']

markFont = Font(name='Calibri', size=11, bold=True)
redFill = PatternFill(start_color='FFFF0000',
                      end_color='FFFF0000',
                      fill_type='solid')
blueFill = PatternFill(start_color='0000FFFF',
                       end_color='000000FF',
                       fill_type='solid')


def drawAtariBg(ws):
    ws_AtariNums = ws
    # Change the name of sheet


    for i in range(1, len(readcsv.key) + 1):
        # 1 到 9  j - 1 0 到 8
        for j in range(0, 9):
            ws_AtariNums.cell(column=1, row=i).value = readcsv.key[i - 1]
            ws_AtariNums.cell(column=1, row=i).font = markFont
            ws_AtariNums.cell(column=2, row=i).value = readcsv.date[i - 1]
            ws_AtariNums.cell(column=j + 3, row=i).value = int(readcsv.num_str_dict[readcsv.key[i - 1]][j])
    ws_AtariNums.insert_rows(1)
    # ws.merge_cells(start_row=2, start_column=1, end_row=4, end_column=4)

    for cell in list(ws_AtariNums.rows)[0]:
        cell.fill = redFill
        cell.font = markFont
    ws_AtariNums['A1'] = row1[0]
    ws_AtariNums['B1'] = row1[1]
    ws_AtariNums['C1'] = row1[2]
    ws_AtariNums[get_column_letter(10) + '1'] = row1[3]
    ws_AtariNums.merge_cells(start_row=1, end_row=1, start_column=3, end_column=9)
    ws_AtariNums.merge_cells(start_row=1, end_row=1, start_column=10, end_column=11)

def DrawAtariNums():
    ws_atari = wb.active
    ws_atari.title = '当選数字'
    drawAtariBg(ws_atari)
DrawAtariNums()

def DrawBG(ws):
    keyLen = len(readcsv.key)
    for i in range(1, 38):
        # 1 - len(key)  1到153 -1 0 -152
        for j in range(0, keyLen):
            ws.cell(column=1, row=j + 1).value = readcsv.key[j]
            # 填满1到37 的数字
            ws.cell(column=i + 1, row=j + 1).value = i


def drawZouShiTu():
    ws_zhoushitu = wb.create_sheet("走势图")
    # 1- 37 column

    DrawBG(ws_zhoushitu)

    for i in range(0, len(readcsv.key)):
        kujiNums = readcsv.num_int_dict[readcsv.key[i]]
        for j in range(0, 7):
            ws_zhoushitu.cell(column=kujiNums[j] + 1, row=i + 1).fill = redFill
        for j in range(7, 9):
            ws_zhoushitu.cell(column=kujiNums[j] + 1, row=i + 1).fill = blueFill

    wb.active = ws_zhoushitu


drawZouShiTu()


# 查看某一期 和 其前y期的数字重合
def CheckRepeatNum(x, y,sheet_name):
    ws_checkReqeatNum = wb.create_sheet(sheet_name)
    drawAtariBg(ws_checkReqeatNum)
    # DrawBG(ws_checkReqeatNum)

    # 要查的这期
    nums = []
    # checkNums = []
    repeatNum = []
    repeatNumDic = {}

    nums = readcsv.num_int_dict[readcsv.key[x]]
    #print(nums)
    for c in range(0,7):
        ws_checkReqeatNum.cell(column=c + 3, row=x + 2).fill = redFill
    # 历遍后面 y 期
    for xIndex in range(0, 7):
        repeatCount = 0
        repeatNumDic[nums[xIndex]] = repeatCount
        for i in range(x + 1, x + y + 1):
            checkNums = readcsv.num_int_dict[readcsv.key[i]]
            # 双循环 查重复
            for yIndex in range(0, 7):
                if nums[xIndex] == checkNums[yIndex]:
                    repeatCount += 1
                    repeatNumDic[nums[xIndex]] = repeatCount

                    ws_checkReqeatNum.cell(column=yIndex + 3, row=i + 2).fill = blueFill

                    # ws_checkReqeatNum.cell(column = ,row = i + 2)

        # for yNum in readcsv.num_int_dict[readcsv.key[i]]:
        #     for xNum in nums:
        #         if xNum == yNum:
        #             repeatCount +=1
        #             repeatNumDic[xNum] = repeatCount
    print(f'最近第{x}期 和 其前{y}期')
    print(repeatNumDic)
    ws_checkReqeatNum.sheet_view.zoomScale = 90
    wb.active = ws_checkReqeatNum

for i  in range(50) :
    CheckRepeatNum(i, 10, f"第{i}期和其前2期")



wb.save(excel_file_temp_Name)

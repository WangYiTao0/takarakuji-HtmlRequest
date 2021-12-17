import readcsv
from GenerateCSVFromUrl import GenerateCSV, remove_specific_row_from_csv, csv_to_xlsx
from readcsv import ReadCSVFile
import openpyxl

url = 'http://www.ohtashp.com/topics/takarakuji/'
csv_file_Name = 'kuji.csv'
excel_file_Name = 'kuji.xlsx'


GenerateCSV(url,csv_file_Name)
kujiData = ReadCSVFile(csv_file_Name)
#csv_to_xlsx(csv_file_Name,excel_file_Name,"2019-2021")

print(kujiData[readcsv.key[0]])

# workbook
# worksheet
# row column cell
wb= openpyxl.load_workbook(excel_file_Name)
ws = wb.active
print(wb.sheetnames)
kuji_19_221 = wb.create_sheet('2019-2021')
print(wb.sheetnames)

#ws = wb.get_sheet_by_name('sheetTitle')

#remove_specific_row_from_csv(fileName,'','')

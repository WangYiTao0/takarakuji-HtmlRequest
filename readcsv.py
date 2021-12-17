import csv

key = []
date = []

num1 = []
num2 = []
num3 = []
num4 = []
num5 = []
num6 = []
num7 = []
bonus1 = []
bonus2 = []

numdict = {}

def ReadCSVFile(csv_file_name) :
    csv_file = open(csv_file_name, mode='r', encoding='utf-8')
    reader=csv.reader(csv_file)
    for item in reader:
        if item[1] != '':
            #print(item[1])
            #newstr = item[1][1:len(item[1])-1]
            #print(newstr)
            #key.append(item[1])
            key.append(item[1])
            date.append(item[2])
            num1.append(item[3])
            num2.append(item[4])
            num3.append(item[5])
            num4.append(item[6])
            num5.append(item[7])
            num6.append(item[8])
            num7.append(item[9])
            bonus1.append(item[10])
            bonus2.append(item[11])
            numList = [int(item[3]), int(item[4]), int(item[5]), int(item[6]),
                int(item[7]), int(item[8]), int(item[9]), int(item[10]), int(item[11])]
            numdict[item[1]] = numList
    csv_file.close()
    return numdict


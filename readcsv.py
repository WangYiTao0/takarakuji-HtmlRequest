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

num_str_dict = {}
num_int_dict = {}


def ReadCSVFile(csv_file_name):
    csv_file = open(csv_file_name, mode='r', encoding='utf-8')
    reader = csv.reader(csv_file)
    for item in reader:
        if item[1] != '':
            # print(item[1])
            # newstr = item[1][1:len(item[1])-1]
            # print(newstr)
            # key.append(item[1])
            key.append(item[1])
            date.append(item[2])
            num1.append(int(item[3]))
            num2.append(int(item[4]))
            num3.append(int(item[5]))
            num4.append(int(item[6]))
            num5.append(int(item[7]))
            num6.append(int(item[8]))
            num7.append(int(item[9]))
            bonus1.append(int(item[10]))
            bonus2.append(int(item[11]))
            num_str_list = [item[3], item[4], item[5], item[6],
                            item[7], item[8], item[9], item[10], item[11]]
            num_int_list =[int(item[3]), int(item[4]), int(item[5]), int(item[6]),
                            int(item[7]), int(item[8]), int(item[9]), int(item[10]),
                                                                       int(item[11])]
            num_int_dict[item[1]] = num_int_list
            num_str_dict[item[1]] = num_str_list
    csv_file.close()
    return num_str_dict

import csv
with open(r'C:\Users\AryanFernandes\Desktop\aryan\project-1\FR_PYCHARM\FR_PYCHARM/Attendance.csv','r')as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line)


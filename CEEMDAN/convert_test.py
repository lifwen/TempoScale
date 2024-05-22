import csv


data_array = []
long=[]
short=[]
data=[]
target=[]

with open('merged_data-.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        long.append(float(row[0]))


with open('0out1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        short.append(float(row[0]))

with open('Machine_usage_groupby_test.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        target.append(float(row[0]))

import csv
for i in range(0, 5550):
    data.append(long[i+1:49 + i]+(short[i:48 + i])+(target[i+193:48+193+i]))


with open('test.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    for row in data:
        csv_writer.writerow(row)

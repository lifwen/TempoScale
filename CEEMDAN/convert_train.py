import csv

data_array = []
long=[]
short=[]
data=[]
target=[]
with open('long_train.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        long.append(float(row[0]))


with open('short_train.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        short.append(float(row[0]))

with open('Machine_usage_groupby.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        target.append(float(row[0]))

import csv

for i in range(0, 19900):
    data.append(long[i:48 + i]+(short[i:48 + i])+(target[i:48+i]))

with open('train.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    for row in data:
        csv_writer.writerow(row)

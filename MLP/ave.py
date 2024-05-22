import csv
import numpy as np

average_values = []
num=48

for file_number in range(0, 1):
    csv_file_path = 'arrays.csv'
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)

        # next(reader, None)
        A=[]
        for row in reader:
            for i in range(0,num):
                A.append((float(row[num+i])-float(row[i]))*(float(row[num+i])-float(row[i])))
        print(np.mean(np.array(A)))


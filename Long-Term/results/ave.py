import csv
import numpy as np

average_values = []
num=48

for file_number in range(0, 1):
    csv_file_path = 'merged_data-.csv'
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        A=[]
        B=[]
        C=[]
        next(reader)

        for row in reader:
            row = [float(value) for value in row]
            C.append((np.corrcoef(row[0:48], row[48:96])[0, 1]) ** 2)
            for i in range(0,num):
                A.append((float(row[num+i])-float(row[i]))*(float(row[num+i])-float(row[i])))
                B.append(max(float(row[num+i])-float(row[i]),-float(row[num+i])+float(row[i]))/float(row[num+i]))


        print(np.mean(np.array(A)))
        print(np.mean(np.array(B)))
        print(np.mean(np.array(C)))

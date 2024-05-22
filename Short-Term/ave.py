import csv

import numpy
import numpy as np

average_values = []
num=48
from sklearn.metrics import mean_squared_error
def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true))

# 循环处理1.csv到10.csv
for file_number in range(0, 1):
    csv_file_path = 'normalized_data.csv'
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        A=[]
        B=[]
        C=[]
        next(reader)

        for row in reader:
            row = [float(value) for value in row]
            C.append((np.corrcoef(row[0:48], row[48:96])[0, 1]) ** 2)
            A.append(mean_squared_error(row[0:48], row[48:96]))
            B.append(mean_absolute_percentage_error(numpy.array(row[0:48]), numpy.array(row[48:96])))



        print(np.mean(np.array(A)))
        print(np.mean(np.array(B)))
        print(np.mean(np.array(C)))

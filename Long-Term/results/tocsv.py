import os

import numpy as np
import csv

data1 = np.load('pred.npy')
data2 = np.load('true.npy')

merged_data = np.column_stack((data1, data2))

with open('merged_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(merged_data)

import csv

with open('merged_data.csv', 'r') as input_file, open('merged_data-.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    for row in reader:
        cleaned_row = [cell.replace('[', '').replace(']', '') for cell in row]
        writer.writerow(cleaned_row)

os.system("python ave.py")
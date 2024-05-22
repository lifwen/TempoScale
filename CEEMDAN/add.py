import csv

def add_csv_elements(csv_file1, csv_file2, output_file):
    with open(output_file, 'w', newline='') as f_out:
        writer = csv.writer(f_out)

        with open(csv_file1, 'r') as f1, open(csv_file2, 'r') as f2:
            reader1 = csv.reader(f1)
            reader2 = csv.reader(f2)

            for row1, row2 in zip(reader1, reader2):
                # Convert elements to float and add them
                row_sum = [float(x) + float(y) for x, y in zip(row1, row2)]
                writer.writerow(row_sum)

csv_file1 = '0out1.csv'
csv_file2 = 'merged_data-.csv'
output_file = 'result.csv'
add_csv_elements(csv_file1, csv_file2, output_file)
print("Result has been written to", output_file)

import csv


with open('long.csv', 'r') as input_file:
    reader = csv.reader(input_file)


    with open('long_train.csv', 'w', newline='') as output_file_1:
        writer_1 = csv.writer(output_file_1)
        for index, row in enumerate(reader):
            if index >= 20000:
                break
            writer_1.writerow([row[0]])

with open('long.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    with open('long_test.csv', 'w', newline='') as output_file_2:
        writer_2 = csv.writer(output_file_2)
        for index, row in enumerate(reader):
            if index < 20000:
                continue
            writer_2.writerow([row[0]])

with open('short.csv', 'r') as input_file:
    reader = csv.reader(input_file)

    with open('short_train.csv', 'w', newline='') as output_file_1:
        writer_1 = csv.writer(output_file_1)
        for index, row in enumerate(reader):
            if index >= 20000:
                break
            writer_1.writerow([row[0]])

with open('short.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    with open('short_test.csv', 'w', newline='') as output_file_2:
        writer_2 = csv.writer(output_file_2)
        for index, row in enumerate(reader):
            if index < 20000:
                continue
            writer_2.writerow([row[0]])
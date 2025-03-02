import csv

file_1 = 'first.csv'
file_2 = 'second.csv'
rows_1 = list()
rows_2 = list()


def unique_rows_from_firth():
    with open(file_1, 'r', newline='') as f_1:
        reader_1 = csv.reader(f_1)
        for row in reader_1:
            if row not in rows_1:
                rows_1.append(row)


unique_rows_from_firth()


def write_rows_in_third_file():
    with open('third.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows_1)


write_rows_in_third_file()


def unique_rows_from_second():
    with open(file_2, 'r', newline='') as f_2:
        reader_2 = csv.reader(f_2)
        for row in reader_2:
            if row not in rows_2:
                rows_2.append(row)


unique_rows_from_second()


def write_rows_in_forth_file():
    with open('forth.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows_2)


write_rows_in_forth_file()
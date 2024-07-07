import csv


rows = set()
# Відкриття CSV-файлу для читання
with open('homework_13_1.csv', newline='') as file_r, open('new_file.csv', 'w') as file_w:
    reader = csv.reader(file_r)
    writer = csv.writer(file_w)
    for row in reader:
        item = ','.join(row)
        if item not in rows:
            rows.add(item)
        else:
            writer.writerows(rows)

# with open('homework_13_1.csv', newline='') as f_1:
#     reader = csv.reader(f_1)
#     for row in reader:
#         item = ', '.join(row)
#         print(item)

# with open('new_file.csv', 'w') as f_2:
#     writer = csv.writer(f_2)
#     writer.writerows()



# pliki csv - dane sa rozdzielone znakiem podzialu (,)
# , ; tab i inne
# Zenek, Marek, Tomek, itp
import csv

# biblioteka do pracy z danynmi typu csv
fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

zipped_dict = dict(zip(fields, row))
print(zipped_dict)
dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.10'},
    {'name': 'Tomek', 'branch': 'cos', 'year': 2, 'cgpa': '9'},
    {'name': 'Zenek', 'branch': 'cor', 'year': 1, 'cgpa': '0.5'},
    {'name': 'Zosia', 'branch': 'coa', 'year': 8, 'cgpa': '00'}
]

filename = 'records.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csv_f:
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(fields)
    # csvwriter.writerow(row)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    # csvwriter.writerow(zipped_dict)
    csvwriter.writerows(dict_list)

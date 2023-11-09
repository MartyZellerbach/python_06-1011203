import csv  # słóży do plików csv w pythonie

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter, dialect.quotechar)

    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x00000142CEB86FE0>  objekt z pamięci

    csv_f.seek(0)  # ustawienie licznika ponownie na 0
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(rows)
print(fields)

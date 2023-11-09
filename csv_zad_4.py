import csv

lista = []

with open('dane.csv', 'r') as file:
    reader = csv.reader(file)
    for i in reader:
        lista.append(i)

print(lista)
print(lista[1])  # ['1', ' Michael', ' New Jersey']
print(lista[1][1])  #  Michael

lista[1][1] = "Radek"  # zaminie Michael na Radek

with open('dane2.csv', 'w', newline="", encoding='utf-8') as file:  # i zapisujemy do dane2.csv
    writer = csv.writer(file)
    writer.writerows(lista)


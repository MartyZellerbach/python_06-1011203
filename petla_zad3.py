# # while - pętla sterowana warunkiem
#
#
# licznik = 0
# while True:
#     print("Komunikat!!!")
#     licznik += 1
#     if licznik > 10:
#         break  # przerwanie bieżącej pętli kiedy wyniesie >10
# print(licznik)  # wynik 11
# licznik = 0
# while licznik < 10:
#     print("Komunikat 2")
#     licznik += 1
# print(licznik)  # 10

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")  # zwraca string
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)
print(lista2)

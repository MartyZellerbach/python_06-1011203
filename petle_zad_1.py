# PĘTLE
# for - pętla iteracyjna
# bierze dane i pokolei po nich się pzemieszcza

import random
from itertools import zip_longest  # ładowanie biblioteki

for i in range(10):  # 0..9
    print(i, end=' ')
# end - znak końca linii (domyślnie \n(enter) powoduje wyświelnienie w pionie) powoduje wyświetlenie liczb w poziomie

for i in range(10):  # po : musi być jakaś komenda
    pass  # nic nie robi

for _ in range(10):  # niema zmienna
    # print(_)
    pass

for i in range(10):  # niema zmienna
    print(i * 2, end=" ")  # 0 2 4 6 8 10 12 14 16 18 9
print()
# losowanie liczb z wykorzystaniem remove na liście z użyciem pętli for
# zaimportować random
# wygenerować liczby od 1 .. 49
# w pętli pibierać(losować0 z listy, wyświetlić i usuwać

lista = list(range(1, 50))
lista_wynik = []
for i in range(6):
    wyn = random.choice(lista)
    lista.remove(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [31, 41, 35, 17, 12, 44]
# posortować
lista_wynik.sort()
print(lista_wynik)  # [12, 17, 31, 35, 41, 44]
lista_wynik.sort(reverse=True)  # sortuje i odwraca
print(lista_wynik)  # [42, 33, 32, 23, 21, 20]
lista_wynik.reverse()  # tylko odwraca
print(lista_wynik)  # [20, 21, 23, 32, 33, 42]

for i in range(10):
    if i % 2 == 0:  # % - modulo - reszta z dzielenia
        print(i, "jest parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]  #
print(lista3)  # [0, 2, 4, 6, 8]
print(type(lista3))  # <class 'list'>

lista3 = [j for j in range(1, 10) if j % 2 == 0]  #
print(lista3)  # [2, 4, 6, 8]   - bez zera 0 liczby parzyste
print(type(lista3))  # <class 'list'>

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0 bo float zawsze przy dzieleniu
a %= 2  # a = a % 2
print(a)  # 1.0 reszta z dzielenia

imiona = ['Radek', 'Zenek', 'Tomek']

for p in imiona:
    print(p)
# wyświelić elementy z takiej listy imion z numerem indeksem
# 0 Radek itd.

for p in imiona:
    print(imiona.index(p), p)

for i in range(len(imiona)):  # range(3)
    print(i, imiona[i])

# enumerate() - numeruje kolekcje, zwraca nadany indeks i elemnt
for p in enumerate(imiona):
    print(p)
# wynik pojawia się w KROTKA:
# (0, 'Radek')
# (1, 'Zenek')
# (2, 'Tomek')
a, b = (0, 'Radek')
print(a, b)
# for p, o in enumerate(imiona):  # enumerate ponurowanie kolekcji, a rozpakowanie krotki podczas pobierania danych w petli
#     print(p, o)
for p, o in enumerate(imiona, start=1):  # startuje od 1 dla Radka
    print(p, o)
# lub
for p, o in enumerate(imiona, start=1):  # startuje od 2 czyli od Zenka
    if p >= 1:
        print(p, o)
# lub
for i in range(1, len(imiona)):  # range(3)
    print(i, imiona[i])

ludzie = ['Radek', 'Janek', 'Asia', 'Romek', 'Artur']
wiek = [47, 57, 32, 34]
# wypisaniu imienia i opodiwajacego mu wieku
# # gdy długość list różne:
# for x in range(len(ludzie)):
#     print(ludzie[x], wiek[x])
#
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])
#
for i in zip(ludzie, wiek):
    print(i)
# dostajemy krotke
# rozpakujemy ta krotke
# for o, w in zip(ludzie, wiek):
#     print(o, w)  # domyślnie daje spacje pomiedzy np. radek 47

for o, w in zip(ludzie, wiek):
    print(o, w, sep=";")
# Radek;47
# Janek;57
# Asia;32
# Romek;34
# sep - znak separacji pmizy przecinkami(domy slnie spacja)

# 0 Radek 47
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (3, ('Romek', 34))
#
# a, b = (3, ('Romek', 34))
# print(a)
# print(b)  # ('Romek', 34)
# imie, wiek = ('Romek', 34)
# indeks, (imie, wiek) = (3, ('Romek', 34))
# print(indeks, imie, wiek)  # 3 Romek 34

a, b = (3, ('Romek', 34))
print(a)
print(b)  # ('Romek', 34)
imie, wiek2 = ('Romek', 34)
indeks, (imie, wiek2) = (3, ('Romek', 34))
for indeks, (imie, wiek2) in enumerate(zip(ludzie, wiek)):
    print(indeks, imie, wiek2)  # 3 Romek 34
# 0 Radek 47
# 1 Janek 57
# 2 Asia 32
# 3 Romek 34
# teraz mamy 5 imion ale tylko dla czterech osób wiek
# łądujemy biblioteki longest

zipped = zip_longest(ludzie, wiek, fillvalue='Nan')
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)
for name, age in zipped_list:
    print(name, age)
# Radek 47
# Janek 57
# Asia 32
# Romek 34
# Artur Nan
# dodać indeksy
for p in enumerate(zipped_list):
    print(p)
for i, (o, w) in enumerate(zipped_list):
    print(i, o, w)
# 0 Radek 47
# 1 Janek 57
# 2 Asia 32
# 3 Romek 34
# 4 Artur Nan

c = {'name': 'Radek', 'age': '5'}  # słownik
print({v: k for k, v in c.items()})  # {'Radek': 'name', '5': 'age'}

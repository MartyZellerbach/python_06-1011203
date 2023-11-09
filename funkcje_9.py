def odejmij(a, b):
    return a - b
# funkcja zwraca wynik odejmowania

print(odejmij(7,8))

# funk lambda - skrócony zapis funkcji

odejmij = lambda a, b: a - b  # lambda zwraca wynik
print(odejmij(9, 7))  # 2

def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100

oblicz_vat2 = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat2(1000))
print(oblicz_vat2(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "doroscly")
print(wiek(8))
print(wiek(10))
print(wiek(18))

lista = [1, 2, 3, 4, 5, 6, 20, 25, 50, 80]
l = []
for i in lista:
    l.append(i * 2)
print(l)

# map() bieże kazdy element, zmienić elemety wg zadanej funkcji

def zmien(x):
    return x * 2

print(f"Zastosowanie map(): {list(map(zmien, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")

print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}")
# x > 3 i x < 20
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")


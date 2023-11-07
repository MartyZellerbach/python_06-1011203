# krotka (tupla0 - niemodyfikowalna
# leprze wykorzystywane pamięci przez pythona podczas używania krotek
# ktorka może byc jednoelementowa - wypełnia znamiona zmiennej (niezmiennej)
# krotki nie można też sortować

tuple = "Radek",
temp = 36, 6
print(type(tuple))  # <class 'tuple'>
print(type(temp))  # <class 'tuple'>

tupla2 = "Tomek", "Asia", "Zbyszek", "Marek"
print(type(tupla2))
print(tupla2)

tupla3 = (43, 55, 22.34, 11, 200)
print(tupla3)
print(type(tupla3))  # <class 'tuple'>

print(tupla2.index('Tomek'))
print(tupla2.count('Asia'))

# rozpakowanie tupli(krotki)
a, b = 1, 2
print(a)
print(b)

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3
print(a)  # 1
print(b)  # [2, 3] worek na reszte danych

# "Tomek", "Asia", "Zbyszek", "Marek"
imie, *imie2, imie3 = tupla2
print(imie2)
print(imie)
print(imie3)

lista = list(tupla2)
print(lista)  # ['Tomek', 'Asia', 'Zbyszek', 'Marek']
print(type(lista))  # <class 'list'>




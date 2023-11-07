#  set (zbiór) - przechowuje niezduplikowane elementy

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista) # z,miana na set
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}  - nie zachowuje kolejnosci przy dodawaniu elementu, zmienil sie rozniez nawias na klamerkowy
# pusty set() jest słowo set()
zb2 = set()  # tworzenie pustego seta
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

zb2.add(2)
zb2.add(3)
zb2.add(4)
zb2.add(5)
print(zb2)  # {2, 3, 4, 5}

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}
zbior.pop()
zbior.pop()
zbior.pop()
print(zbior)  # {44, 18, 22, 55}  usunal trzy ostatnie ze zbioru

zbior.remove(55)  # usuwamy 55
zbior.remove(18)  # usuwamy 18
print(zbior)  # {44, 22}

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}

print(zbior | zbior2)  # suma dwóch zbiorów {999, 11, 44, 18, 52, 22, 667, 62} z uwzgledniemiem ze jak powtarzaja sie dane to pokaze tylko raz
print(zbior & zbior2)  # {44} - część wspólna
print(zbior - zbior2)  # różnica {22}
print(zbior.difference(zbior2))  # różnica {22} to samo co wyżej

# Ćwiczenie własne
zbior3 = {1, 2, 3, 4, 5, 5}
print(zbior3)
zbior3.add(15)
zbior3.add(0)
zbior3.add(115)
print(zbior3)  # {0, 1, 2, 3, 4, 5, 115, 15}














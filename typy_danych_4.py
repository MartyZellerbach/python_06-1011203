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





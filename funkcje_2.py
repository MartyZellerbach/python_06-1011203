# funkcja zwracające wynik
def dodaj(a, b):
    return a + b  # return zwraca wynik


print(dodaj(5, 6))


# funkjce która posiada trzy argumenty zwraca wynik np. odejmowanie
# jeden argument wartość domyślna
# użyć ją na kilka sposobów

def odej(a=0, b=0, c=0):
    print(a - b - c)
    return a - b - c  # return zwraca wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(odej(5, 6, 9))
print(odej(c=5, b=0))
print(odej(5, 6))
print(odej(c=5, a=6, b=1))
print(dodaj(4, 6) * odej(6, 9, 9))
print(oblicz_vat(10000, 9))
print(oblicz_vat(vat=10000, cena=9))  # domyślną wartość można podawać np. patrz vat
print(oblicz_vat(vat=8, cena=1000))
# print(odej(b=8, c=9, 2))  # jak podajemy argumenty to musimy podawać do konca b.. c.. oraz a..  SyntaxError: positional argument follows keyword argument

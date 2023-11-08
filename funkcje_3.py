# użycie zmiennych globanych na zew i wew funkcji

a = 10
b = 10


def dodaj():
    a = 6  # zmienne loklane, bez wpływu na zmienne globalne, zakres w odrębie tej funkcji
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # wewnątrz funkcji uzyje zmiennej globalnej, każda zmiena w funkcji wartości tej zmiennej zmienia wartość tej zmiennej globalnie
    a = 6
    b = 7
    print(a + b)


print(f"Zmienna a z góry (globalna) {a}")
dodaj()
print(f"Zmienna a z góry (globalna) {a}")
dodaj2()
print(f"Zmienna a z góry (globalna) {a}")
dodaj3()
print(f"Zmienna a z góry (globalna) {a}")
dodaj2()

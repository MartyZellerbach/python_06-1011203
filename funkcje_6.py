# napisanie funkjcji która oblicza średnia np. ocen
def liczby(name=None, *cyfry):  # dowolna ilość argumentów typu pozycyjnego
    # print(cyfry)
    suma = 0
    count = len(cyfry)
    try:
        for c in cyfry:
            suma += c  # suma = suma + c
        print(f"Średnia wynosi {suma / count}.")
    except ZeroDivisionError:
        print(f"Uczeń {name} nie ma ocen.")
    except Exception as e:
        print("Błąd", e)

def liczby2(*cyfry, name=None):
    print(cyfry)
    print(name)

liczby()  # tu będziue uczeń None bo nie podane są dane
liczby(1)
liczby(2, 3)
liczby(1, 2, 3, 4, 5, 6, 7)
liczby("Tomek", 1, 2, 3, 4, 5, 6, 7)
liczby2(1, 2, 3, 4, 5, 6, 7)
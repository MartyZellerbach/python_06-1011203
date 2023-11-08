# funkcja - wydzielony fragment kodu który mozna wykonać wielokrotnie
# funkcja kalkulator - w dowolnym miejscu wykonać albo np. słownik itd.

a = 6  # zmienne globalne w głównym scopie
b = 7


# dwie linie odstępu, u góru defaultowo! Funkcja musi być zdeklarowana przed użyciem
# dane ze scopa głównego (wyższego) będą widoczne
def dodaj():  # miejsce deklaracji trzeba jeszcze wywołać tą funkcje - funkcja bezargumentowa
    c = 7  # c nie będzie widoczne poza ta funkcja (w wyższym scopie (zakresie)) - zmienna lokalna w funkcji
    print(a + b)


def dodaj2(a, b):  # a,b zaekltrowane w fukncji z waretościa domyslna
    print(a + b)


def odejmij(a, b, c=0):  # c=0 paramtr z wartością domuyslna
    print(a - b - c)


# użycie/urchomienie funkcji - nazwa fukncji, nawiasy (), ewentualnie w nawiasach argumenty
dodaj()  # 13 - miejsce wykonania funkcji
dodaj2(8, 9)
odejmij(1, 2, 3)  # wywołanie ze wsystkimi parametrymi
odejmij(1, 2)  # wywołanie z domyślnym c = 0
odejmij(b=9, a=8)  # argumenty przekazane po nazwie
odejmij(c=9, b=3, a=9)  #
dodaj2(b=8, a=9)
dodaj2(b=-8, a=+9)
odejmij(b=-9, a=-8)  # argumenty przekazane po nazwie

print(dodaj() + odejmij(6 ,9))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

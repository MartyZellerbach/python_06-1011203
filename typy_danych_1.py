wiek = 47  # int
rok = 2023  # int
temp = 46.6  # float
wiek2 = 37.5
# wiek = 37,5  <--- nie stosować, to nie jest liczbap
print(wiek)
print(type(wiek))
print(wiek2)
print(type(wiek2))
print(rok)
print(type(rok))
print(temp)
print(type(temp))

print(5 * "Radek")
print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)  # wynik dzielenia zawsze będzie typem danych float

print(wiek // rok)  # część całkowieta z dzielenia
print(wiek % rok)  # reszta z dzielenia czyli modulo 47

print(5 % 2 )  # 1 bo 2 * 2 = 4 + 1 = 5   dzielenie 5/2 daje wynik 1
print(wiek ** rok)
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999...
# flouty i obliczenia wystepuje bład zaaokrąglenia - wynika to z pamęci przehcowywaia w pamięci komputera
# flouty mają błąd zaokrąglenia
print(f"{0.2 + 0.7:.1f}") # 0.9
#  w jakich typach danych przechowywać pieniadze w javie ?  bigdecimal lub decimal
print(f"Sprawdzenie zmiennej {temp} {wiek}")
print(f"""
{wiek}
    {temp}
""")

# tym logiczny
# True lub False   - DUŻE LITERY OBOWIĄZAKOWO

czy_znasz_python = False
print(czy_znasz_python)
print(type(czy_znasz_python))  # <class 'bool'> czyli typ logiczny
print(int(czy_znasz_python)) # 1
# zamiana w drugą strone czyli 1 na True, 0 - True
x = 1
print(bool(x))  # True
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = 0
print(bool(x))  # False
x = ''
print(bool(x))  # False
x = 'Radek'
print(bool(x))  # True
x = None  # stan nieokreślony
print(bool(x))  # False
# nie uzywamy w zmienych polskich iter

# działania logiczne
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# not - negacja
print(not False)  # True
print(not True)  # False
x = 1
print(not x == 1)  # False

# warunki

a = 8
b = 7
print(f"Porównanie {a} > {b}", a > b)
print(f"Porównanie {a} < {b}", a < b)
print(f"Porównanie {a} == {b}", a == b)  # porównanie czy a równa się b
print(f"Porównanie {a} != {b}", a != b)  # czy różne
print(f"Porównanie {a} >= {b}", a >= b)
print(f"Porównanie {a} <= {b}", a <= b)
# stackoverflow
# chatgpt






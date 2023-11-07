# klucz - wartosc
# typ danych gdzie mamy: { 'klucz' : 'wartosc' }  gdzie klucz nie może się powtarzać
# słownik - typ daych o budowie parta klucz - wartosc

dictionary = {}  # tworzenie pustego słownika
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'> pusty slownik

# cos dodajemy do slownika

# nazwa klucza jest indeksem  klucz imie - wartosc Radek
dictionary['imie'] = 'Radek'
print(dictionary)
dictionary['wiek'] = '35'
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(
    dictionary.items())  # krotka  dict_items([('imie', 'Radek'), ('wiek', '35')]) - bo wyswietla w nawiasach okraglych i sa przecinki
# print(dictionary.items())
# dodawanie
dictionary.update({'date': '12-12-2023'})
print(dictionary)  # {'imie': 'Radek', 'wiek': '35', 'date': '12-12-2023'}

dict2 = {'x': 2}
dict2.update([("y", 5), ("z", 7)])
print(dict2)  # {'x': 2, 'y': 5, 'z': 7}

# Utworzy słownik gdzie beda pary polskie słowo-angielskie tłumaczenie

dict_p_e = {'imie': 'name', 'kot': 'cat'}
print(dict_p_e['imie'])

# pokazemy jakie slowa umimey tłumaczyć
# zapytamy użytkownika jakie słowo chce przetłumaczyć
# wypiszemy mu tłumaczenie
print(f"Umiem przetłumacyzć: {dict_p_e.keys()}")
key = input("Podaj słowo do przetłumaczenia:")
print(dict_p_e[key.replace(" ",
                           "").lower()])  # wpisze słowo w terminalu kot i przetłumaczył na cat + zamieniamy spacje oraz zamiermiany duze litery lower

# Napisać kalkulator
# pobrać dane a i b od użytkownika
# wyświetlić wunik działania np. dodawania

a = input("Podaj pierwszą liczbę:")  # input zwraca str
b = float(input("Podaj drugą liczbę:"))  # input zwraca str dodajemy float
print(type(a))  # <class 'str'>
print(int(a) + b)  # kalkulator dodawanie

# BTW hackerrank - ćwieczenia na www
print(eval("5 + 5"))

a = "6"
b = "6"
wyr = a + "+" + b
print(eval(wyr))  # wynik 13

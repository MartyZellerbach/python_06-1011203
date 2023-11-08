# napisać program kalkulator z wykorzystaniem pętli while True jako głównej pętli programu
# menu startowe - z dostepami działania
# pobrać wybrane opcje
# pobrać od uzytkownika liczby
# wyświetlić wynik
# dodać sposób wyjścia z programu
#

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")
    odp = input('Podaj wybranoą opcje ')  # zwraca str
    #    choice = int(input("Wybierz opcje z menu (1-5):"))

    if odp >= '5':
        break
    a = float(input('Podaj pierwszą liczbę '))
    b = float(input('Podaj drugą liczbę '))

    if odp == '1':
        print(f"Wynik dodawania {a} + {b} = {a + b}")
    elif odp == '2':
        print(f"Wynik odejmowanie {a} - {b} = {a - b}")
    elif odp == '3':
        print(f"Wynik mnożenie {a} * {b} = {a * b}")
    elif odp == '4':
        print(f"Wynik dzielenia {a} / {b} = {a / b}")
    else:
        print("Nie znam takiego działania...")

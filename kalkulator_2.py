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
    try:
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
            print("Nie znam taking działania...")
    except ZeroDivisionError:
        print("Nie dziel przez zero!!!")
    except ValueError:
        print("Błąd wartości, wpisz liczbę w działaniu!")
    except TypeError:
        print("Błąd typu")
    except Exception as e:  # pozostałe wyjątki
        print("Wsytapił błąd", e)
    else:  # wykona się tylko, gdy nie wystąpi błąd
        print("Operacja zakończyła się pomyślnie")
    finally:
        print("To wykona się zawsze..")
        print("Zakończyłem obliczenia..")
# jaki sposób przechwytujemy wyjątki w pythoni ? try - except, ewentualnie finally
# praca domowa - za pomocą case
# shift + tab - zaznaczone linie cofa, do lewej..


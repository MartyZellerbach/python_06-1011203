user = "Nuda"  # str
wiek = 42  # int
wersja = 3.90001  # float liczba zmiennoprzecikowa
# ograniczenie w pythton to 4tys cyft - poza maks 4tys cyfr
liczba = 123456789987654321  # int
print("Witaj %s masz teraz %d lat(a)" % (user, wiek))
# print("Witaj %d masz teraz %s lat(a)"  % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - strind
# %d - digit całkowita
print("Witaj %(user)s, masz teraz %(wiek)d lat(a)." % {'user': user, 'wiek': wiek})
print(f"Witaj {user}, masz teraz {wiek} lat(a).")  # f - f-string
# Witaj Nuda, masz teraz 42 lat(a).
print(f"Witaj {wiek}, masz teraz {user} lat(a).")  # f - f-string
# Witaj 42, masz teraz Nuda lat(a).
# LICZBY
print("Używamy wersji Pythona %i" % 3)
print("Używamy wersji Pythona %f" % 3.8)  # Używamy wersji Pythona 3.800000
print("Używamy wersji Pythona %.1f" % 3.8)  # Używamy wersji Pythona 3.8
print("Używamy wersji Pythona %.2f" % 3.8)  # Używamy wersji Pythona 3.80
print("Używamy wersji Pythona %.0f" % 3.8)  # Używamy wersji Pythona 4
# zaokragla przy wypisywaniu
print("Używamy wersji Pythona %.f" % 3.8)  # Używamy wersji Pythona 4
print("Używamy wersji Pythona {}".format(wersja))
print(f"Używamy wersji Pythona {wersja:.1f}")
print(f"Używamy wersji Pythona {wersja:.2f}")
print(f"Używamy wersji Pythona {wersja:.0f}")
#
print(f"{user:>10}")  # Nuda  wyrównał do prawej na 10
print(f"{user:>20}")  # Nuda  wyrównał do prawej na 20
print(f"{user:<20}")  # Nuda
print(f"{user:^10}")  # wyśrodkowanie
#
print(liczba)  # 123456789987654321
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 123,456,789,987,654,321
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 123.456.789.987.654.321
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 123 456 789 987 654 321
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # liczba 123 456 789 987 654 321
#  : oddzielenie zmiennej od parametru

# c.d. warunki_1

suma_zam = 100
if suma_zam > 150:  # komenda if musi się zakończyć :
      rabacik = 25
else:
      rabacik = 0

print(f"Rabacik wynosi: {rabacik}")

# inaczej napisane
suma_zam = 100
rabat = 25 if  suma_zam > 150 else 0
print(f"Rabacik wynosi: {rabat}")
#wyniki
# Rabacik wynosi: 0
# Rabacik wynosi: 0

# zasymuujemy system zbierania logów
# w zależności od systemu i od logu to my będziemy mieli różny komunikat

list_bledow = []
alert_system = "console"
error = "info"
error_message = "Stało się coś strasznego"
# gdy system email - wyświetlić te nasz komunikat
if alert_system == 'email':
    print(error_message)
elif alert_system == 'console':
    if error == 'medium':
        list_bledow.append("ostrzeżenie")
    elif error == 'critical':
        list_bledow.append("krytyczny")
    else:
        list_bledow.append("inny")
print(list_bledow)

# ćwieczenie na if
# zrobić test z historii czegokolwiek
# zadać pytanie
# pobrać odpowiedz
# sprawdzić
# wypisać ocene

odp = input("Podaj stolicę Polski?")
if odp.capitalize() == 'Warszawa':
    print("Prawda")
elif odp.capitalize() == 'Kraków':
    print("To chyba nie to miasto, wygoogluj proszę.")
else:
    print("Pomyliłeś się, musisz się douczyć..")

odp2 = input("W którym roku był chrzest Polski")
if odp2.capitalize() == '966':
    print("Prawda")
else:
    print("Pomyliłeś się, musisz się douczyć..")










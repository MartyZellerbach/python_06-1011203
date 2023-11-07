# warunki
# uzalezniają działanie programu na podstawie warunku
# if - jeżeli - instrukcja sterowania przepływem programu
# jakie znasz instreukcje sterowania programu ? np if

# narzucamy odpowiedz np. True
odp = True
if odp:
    print("Brawo")
print("Idę dalej")

# w przypadku narzucania False else, czyli jeżeli jest coś źle to przeżuci nas na print Ucz sie dalej.
odp = False
if odp:
    print("Brawo")  # gdy spełniony warunek
else:
    print("Ucz się dalej")  # w przeciwnym przypadku

podatek = 0.9
zarobki = int(input("Podaj dochów"))  # podaj dochów zamieniamy na liczbę całkowitą int
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.9
print(f"Płacisz {zarobki * podatek}")

# dla 10.000 do 29.999 podatek 0.2
# kolejność warunków ma znaczenie
podatek = 0.9
zarobki = int(input("Podaj dochów"))  # podaj dochów zamieniamy na liczbę całkowitą int
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:  # dla 10.000 do 29.999 podatek 0.2 <- dodajemy tutaj
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.9
print(f"Płacisz {zarobki * podatek} podatku")


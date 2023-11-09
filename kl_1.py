# klasy - szablon (przepis, opis) wg którego będziemy budować obiekty
# klasa może posiadać pola (zmienne), funkcje (metody)
# oiekt element zbudowany na podstawie klasy
# obiekt jest instancją klas


class Human:
    """
    Klasa opisująca Człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print(f"Wiek: {self.wiek}")


# wyswietlenie dokumentacjo dotyczacej klasy/funkcji
print(Human.__doc__)  # Klasa opisująca Człowieka w Pythonie
print(print.__doc__)

# klasy - szablon (przepis, opis) wg którego będziemy budować obiekty
# klasa może posiadać pola (zmienne), funkcje (metody)
# oiekt element zbudowany na podstawie klasy
# obiekt jest instancją klas
# nazwa klasy, niepotrzebuje nawiasów, Human human dwie oddzielne klasy - rozróznia małe i duże litery weg instrukcji
# klasy zakłądamy z duzych liter


class Human:
    """
    Klasa opisująca Człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        """dokumentacje. Klasa wypisuje imie obiektu z klasy Human
        :return: None"""
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Wiek: {self.wiek} lat")


cz1 = Human()  # cz1 obiekt - tworzenie obiektu klasy
# print(Human.__doc__)
# print(print.__doc__)
# print(cz1.plec)
# print(cz1.wiek)
# print(cz1.imie)
cz1.imie = "Ania"
cz1.wiek = 28
print(cz1)  # <__main__.Human object at 0x000001E9B5FA5750>
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)

cz2 = Human()
# print(cz2.imie)
# print(cz2.wiek)
# print(cz2.plec)
cz2.imie = "Michal"
cz2.wiek = "42"
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)

cz2.nazwisko = 'Kowalski'
print(cz2.nazwisko)

cz1.powitanie()
cz1.wypisz_wiek()
cz2.powitanie()
cz2.wypisz_wiek()

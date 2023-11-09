# self oznacza obiekty które wywołuje metody lub pola
class Human:
    """Klasa opisująca człowieka w pythonie"""

    def __init__(self, imie, wiek, plec="k"):  # inicjalizator, konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print(f"Mam na imię {self.imie}")

    def wypisz_wiek(self):
        print(f"Wiek: {self.wiek}")

    def wypisz_plec(self):
        print(f"Plec: {self.plec}")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Ania", 29)
print(cz1.wiek)
print(cz1.plec)
print(cz1.imie)
cz1.powitanie()
cz1.wypisz_wiek()
cz1.wypisz_plec()

cz2 = Human("Radek", 45, "m")
cz2.wypisz_plec()

cz1.ruszaj()
cz2.ruszaj()


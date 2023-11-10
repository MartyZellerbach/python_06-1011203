class Dom:
    """
    Klasa opisująca dom w pythonie.
    """

    def __init__(self, name, metraz, kolor, liczba_okien):  # inicjalizator, konstruktor
        self.__name = name
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def wyswietl_name(self):
        print(f"Name {self.__name}")

    def wyswietl_metraz(self):
        print(f"Metraż {self.__metraz}")

    def wyswietl_kolor(self):
        print(f"Kolor {self.__kolor}")

    def wyswietl_okna(self):
        print(f"Liczba okien {self.__liczba_okien}")

    def zmien_metraz(self):
        wyn = int(input("Podaj metraż: "))
        self.__metraz = wyn
        self.wyswietl_metraz()

    def zmien_okna(self):
        wyn = int(input("Podaj liczbę okien: "))
        self.__liczba_okien = wyn
        self.wyswietl_okna()

    def zmien_kolor(self):
        wyn = input("Podaj kolor: ")
        self.__kolor = wyn
        self.wyswietl_kolor()

dom1 = Dom("Radek", 300, "Biały", 17)
dom1.wyswietl_okna()
dom1.zmien_metraz()
dom1.zmien_kolor()

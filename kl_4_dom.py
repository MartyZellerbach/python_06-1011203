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

dom1 = Dom("Radek", 300, "Biały", 17)
dom1.wyswietl_okna()


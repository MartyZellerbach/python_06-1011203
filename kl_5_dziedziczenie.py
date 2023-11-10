# dziedziczenie
# przejmowanie lub zamiana  z klasy wyższej w naszej klasie


class Pojazd:
    """
    klasa opisująca pojazd
    """

    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # klasa dziedziczy po klasie Pojazd
    """
    Samochod
    """

    def __init__(self, kolor, marka):  # inicjalizator dla klasy samochod
        # pass
        super().__init__(kolor)  # wywołanie inicjalizatora z klasy wyzszej
        self.marka = marka

    def info(self):
        """
        metoda informujaca o cechach obiektu
        :return: None
        """
        # print(f"{self.marka} : {self.kolor}")
        super().info()  # można uzyc metody z klasy wyzszej
        print(f"Samochód: {self.marka}")


# f - formatowanie stringow
poj1 = Pojazd("biały")
poj1.info()  # Kolor: biały

poj2 = Samochod("biały", "Ferrari")
poj2.info()

lista = [poj1, poj2]
for i in lista:
    i.info()

print(poj1.__doc__)  # wyswietlenie dokumentacji dla poj1
print(poj2.__doc__)  # wypisanie dokumentacji klasy
print(poj2.info.__doc__)

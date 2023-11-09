class Car:
    """
    Kklasa opisująca samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def hamuj(self):
        self.__predkosc -= 5

    def __zmien_bieg(self):  # podkreslnikami oznaczamy metody prywatne
        print("Zmiana biegu")

    def licznik(self):
        print(f"Jedziesz z szybkością {self.__predkosc} km/h")


car1 = Car("Fiat", 2023)
car1.gaz()
car1.licznik()
car1.gaz()
car1.gaz()
car1.licznik()
car1.gaz()
car1.licznik()
car1.gaz()
# print(car1.__predkosc)
car1.licznik()
# car1.__predkosc = 200
car1.licznik()
# car1.__predkosc = 0
car1.licznik()
car1.hamuj()
car1.licznik()
car1.hamuj()
car1.licznik()
car1.hamuj()
car1.licznik()

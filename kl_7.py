# wielodziedziczenie
# w pythonie mozemy dziedziczyc na raz po wielu klasach

class A:
    def method(self):
        print('Metoda z klasy A')


class B:
    def method(self):
        print('Metoda z klasy B')

    def method2(self):
        print('Metoda z klasy B')


class C(A, B):
    """Klasa C"""

    def method(self):
        print('Metoda z klasy C')  # metoda z C
        super().method()  # mtoda z A
        B.method(self)


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()
print(C.__mro__)  # kolejność rozwiązywania nazw,  (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
c.method2()

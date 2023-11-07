print()  # wypisz/drukuj
# ctrl +alt l - sprawdza wsystkie zasady! sprwdza cały kod i zapisuje pik
# pep8
print("Nazwyam się Michał M")
print("Dowolny tekst")  # ctrl d - powielanie linii
print("Dowolny tekst")  # można stosować pojedyńcze cudzysłowy
print("Dowolny tekst")
print('można stosować pojedyńcze cudzysłowy')
# 'można stosować pojedyńcze cudzysłowy'' - to jest str string tekst
print(44)
print(type("Michał"))
print(type(44))
print(type("44"))
print("44" + "33")
print(4 * "33")
# rzutowanie w przypadku niewiedzy jakiego typu są dane:
print(int("33") + int("12"))
# silne typowanie - sam z siebie nie zmienia typu
# int() - rzutowanie na int
# zmienna - to taki pojemnik - rano może być na breudne ubrania a wieczorem na czyste
# type - sprawdzenie typu danych
imie = "Mchał"
print(imie)
print(type(imie))  # <class 'str'>

wiek = 42
print(wiek)
print(type(wiek))

imie = 42
print(type(imie))

imie = "Olaaa"
print(imie + wiek)  # TypeError: can only concatenate str (not "int") to str
print(imie + str(wiek))
# skrót klawiszowy ctrl / dodanie chasz / zakomentowanie linii
# str() - rzutowanie na string

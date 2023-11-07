teksty = "Witaj świecie"
print(teksty)  # Witaj świecie
# chcemy dużymi literami wyświetlić
print(teksty.upper())  # WITAJ ŚWIECIE
# zmienna jest nierootowalne czyli nadal przechowuje orginalna wersje napisu czyli małymi literami
# Ctrl + lewy przycisk myszy najeżdzamy na upper
# nie zostaje zmieniony orginalny tekst, tylko dostjemy kopie ze zmianą
# zmieniamy i zapamietujemy zmiane na duże
teksty2 = "DUŻE litery"
tekst2 = teksty2.upper()
print(tekst2)
# zmieniamy i zapamietujemy zmiane na małe
teksty3 = "Małe litery"
tekst3 = teksty3.lower()
print(tekst3)
print(teksty.removeprefix("Witaj"))  # Wycina Witaj
print(teksty.removesuffix("świecie"))  # Wycina świecie
print(teksty)
# policzyć ilość wystąpienie literki i
print(teksty.count("i"))  # county
# zliczanie w przedziale
print(teksty.count("i", 0, 4))  # county
# Witaj świat lolek
# 012345678910...
print(teksty.count("j", 0, 4))  # county 0,4 bierze indeksy od 0 do 3 czyli trzeba dać do 5
print(teksty.count("j", 0, 5))  # i tutaj już znajdzie nam jedną "j"
# kodowanie znaków,
encoded_s = teksty.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie' xc5 jakaś wartośc zapisana w zapisie 16stkowym
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie
# Witaj świecie

imie = "Nuda"
print(imie)
# f - string - sformatowany string czyli tekst sformatowany
tekst_format = f"Mam na imię {imie}"
print(tekst_format)

# nowa linia \n
imie = "Nuda"
print(imie)
# f - string - sformatowany string czyli tekst sformatowany
tekst_format = f"\tMam na imię {imie}\n i lubię pythona\b"
print(tekst_format)
#  \t tabulator  - standardowo cztery spacja
#  \n nowa linia
#  \b backspace/delete

# starsze formatowanie tekstu

starszy = 'witaj %s!'
print(starszy % imie)  # witaj Nuda!
print("Witaj {}!".format(imie))
print("""
    Tekst
    Wielolinijkowy
    """)

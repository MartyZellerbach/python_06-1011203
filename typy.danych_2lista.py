# lista - kolekcja, przechowywać na raz różne typy np. int, float, txt
# zapamiętuje/zachowuje kolejność dodawania !

lista = []  # pusta lista
print(type(lista))  # <class 'list'>

lista.append("Nuda")
lista.append("Nuda1")
lista.append("Nuda2")
lista.append("Nuda3")
print(lista)  # ['Nuda', 'Nuda1', 'Nuda2', 'Nuda3']   lista w kwadratowych nawiasach
#                 0(-4)    1(-3)     2(-2)   3(-1)
# indeksowania od 0
print(lista[0])
print(lista[2])
# wypisać dwa dowolne
print(lista[2], lista[3])
print(lista[3])
print(len(lista))  # 4 czyli trzeba odjąć 1
print(lista[-1])  # wyświetli ostatni element z listy
print(lista[-3])  # Nuda_1
print(lista[0:3])  # wyświetli od 0 do 2 - ['Nuda', 'Nuda1', 'Nuda2']
print(lista[0:-2])  # ['Nuda', 'Nuda1']
print(lista[-2:0])  # [] nic nie jest w stanie wyświetlić - idzie zawsze w praw a zero po lewej

# nadpisanie elementu na danym indeksje
lista[2] = "Nuda3a"
print(lista)

# dodanie we wskazanym miejscu
lista.insert(1, "Nuda")
print(lista)

# usunięcie elementu (pierwszego napotkanego)
lista.remove("Nuda")
print(lista)

# Sprawdzenie indeksu dla elementu
indeks = lista.index("Nuda3")
print(indeks)

# usuniecie elementu po indeksie  czyl;i powyżej zmienna indeks = Nuda3 czyli usuwa Nuda3
print(lista.pop(indeks))  # zwraca element który usunelismy
print(lista)
print(lista.pop())

a = 1
b = 3
a = b
print(a)
b = 7
print(a)

lista2 = lista
lista3 = lista.copy()  # kopiowanie listy z jednej do drugiej
print(lista)  # kopiowanie refenecje - oznacza adres w pamięci
print(lista2)
lista.clear()  # wyczyssc liste
print(lista2)  # []
print(lista)  # []
print(id(lista))  # 1607261901056
print(id(lista2))  # 1607261901056
print(lista3)  # ['Nuda', 'Nuda1']
print(id(lista3))  # 2116619237440

# deklaracja listy z elementami

liczby = [54, 999, 34, 22, 12.34, 687]
# liczby = [54, 999, 34, 22, 12.34, 687, "A"]   # nie umie sortować str
print(liczby)
liczby.sort()
print(liczby)

lista_osoby = ['radek', 'ola', 'zenek']
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek', 'zenek']
# ale jak dodamy liczbe do tego elementu to sortowanie nie zadziała
lista_osoby.reverse()
print(lista_osoby)  # ['zenek', 'radek', 'ola']
lista_osoby.sort(reverse=True)  # ['zenek', 'radek', 'ola']

print(liczby)  # [12.34, 22, 34, 54, 687, 999]
liczby[3] = 6666  # zamieniamy liczbe 54 na 6666
print(liczby)

# usunac element o indeksie 3, usunac element (liczbe) 34 z tej listy
liczby.pop(3)
liczby.remove(34)
print(liczby)
print(len(liczby))  # 4

tekst = 'Python'
lista_1 = list(tekst)  # list() rzutowanie na listę
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n']  rozpakowanie sekwensji

lista_2 = [tekst]
print(lista_2)  # ['Python']

krotka = tuple(liczby)  # zmiana listy na krotka (tuple)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (12.34, 22, 687, 999)

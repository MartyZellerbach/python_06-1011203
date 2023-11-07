# BTW nie nazywamy plików od samego słowa random!
# biblioteka do działania (generowania) liczb pseidolosowaych
import random

print(random.randint(1, 6))  # przeidział zamkniety bedzie losował od 1 do 6, a nie od 1 do 5. - int 1.. 6
print(random.random())  # 0.3856482628896484   float  losuje od 0 do 0.9
print(random.random()*6)  # float 0 do 5.999999
print(random.randrange(6))  # generuje od 0 do 5 losowe
print(random.randrange(1, 6))  # generuje od 1 do 5

#lista = [5, 7, 45, 34, 56]
#print(random.choice(lista))  # wylosuj element z "lista"

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

#program lotto
lista2 = list(range(1,50))  # generuje liczby od 1 do 49
print(lista2)

wynik = random.choice(lista2)
lista2.remove(wynik)
print(wynik)

print(random.choices(lista2, k=6))  # podajemy ile chcemy losować liczb ale losuje z powtórzeniami czyli 1, 1, 1, 2,3

lista2 = list(range(1,50))  # generuje liczby od 1 do 49
print(random.choices(lista2, k=6))  # losuje z powtórzeniami liczb
print(random.sample(lista2, 6))   # losuje 6 liczb  [6, 14, 20, 24, 33, 39]  bez powtórzeń
print(random.sample(lista2, k=6))   # losuje 6 liczb bez powtórzeń



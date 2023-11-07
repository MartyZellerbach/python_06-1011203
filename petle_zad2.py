dictionary = {'imie':"Radek", 'nazwisko': "Kowalski"}
print(dictionary)  # {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(type(dictionary))  # <class 'dict'>
for k in dictionary:
    print(k)
#imie
#nazwisko
# to samo co wyzej
for k in dictionary.keys():
    print(k)
#teraz wartosci VALUES
for v in dictionary.values():
    print(v)
for i in dictionary.items():
    print(i)
for k,v in dictionary.items():
    print(k, "-->", v)  # to jest strzałeczka żeby się oddzielało, może być i spacja
c = {'name': 'Radek', 'age': '5'}  # słownik
print({v: k for k, v in c.items()})  # {'Radek': 'name', '5': 'age'}

d2 = {}
for key, value in c.items():
    d2.update({value: key})
print(d2)
# {'Radek': 'name', '5': 'age'}
# {'Radek': 'name', '5': 'age'}

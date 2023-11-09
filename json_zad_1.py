# json - para klucz - wartość
# '{"name":"John", "age":30, "car":null}'
# obiekt używany głównie do kumnikacji między systemami# zdarza się że jest używany do konfiguracji w piku

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:  # w - stwórz plik
    json.dump(person_dict, f, indent=4,
              sort_keys=True)  # indent - wciecie w pliku 4 spacje - patrz w pliku nasze_dane, sort_keys - sortowanie alfabetycznie
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
# wypisac klucze, wartosci, itemy
# wypisac imie z tego słownika (name)
print(data.keys())
print(data.values())
print(data.items())
# dict_keys(['age', 'czy_pali', 'name'])
# dict_values([40, None, 'Radek'])
# dict_items([('age', 40), ('czy_pali', None), ('name', 'Radek')])
print(data['name'])  # Radek  odczytanie ze słownika

# zamiana słownika na json
json_text = json.dumps(data)
print(json_text)
# {"name": "Radek", "age": 40, "czy_pali": null}

# zamiana json na słownik
string_json = json.loads(json_text)
print(string_json)


import chardet

# pip install chardet
# oraz po prawej na dole rogu Interpreter settings..

file_path = 'test.log'

with open(file_path, 'rb') as file:  # nie jako tekst ale binarnie otwarcie czyrtanie
    raw_data = file.read()

# dla małej próbki czyli np wystąpienie jednego polskiego znaku ś może mieć błędny odczyt tak jak poniżej Turkish
result = chardet.detect(raw_data)  # próba odszyfrowania kodowania pliku
print(result)  # {'encoding': 'Windows-1254', 'confidence': 0.670697820753897, 'language': 'Turkish'}
# dodajemy ręcznie np. ź i sprawdzamy jeszcze raz
# {'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
encoding = result['encoding']
print(raw_data.decode(encoding=encoding))
# Radek
# Dodane
# Dodane
# Dodane
# DośdaneŹ
# łóęć

# praca z plikami
# kontekst menadżer - np. wykonuje operacje w momencie wystąpienia błędu
# with
#     ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w' ) as fh:  # filehandler - taki skrót
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Jeszcze jeden\n")
# w - kasuje plik gdy istnieje i tworzy na nowo.
with open('test.log', 'w') as fh:  # spowoduje usunięcie starego test.log i utworzenie nowego z napisaem Radek.
    fh.write("Radek\n")

with open('test.log', 'a', encoding='utf-8') as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()
print(lines)
# Radek
# Dodane
# Dodane
# Dodane
# Dośdane


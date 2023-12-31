# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
# nosal, sql
# w pythonie sqllite3 - baza sql w jednym pliku, również może być przechowyuwana w pamięci
import sqlite3


#
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()  # obiekt który komunik się z nami a baza musi być
    print("Baza została podłączona")
except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych", e)
finally:  # wykonuje się zawsze
    if sql_connection:
          sql_connection.close()
          print("Baza została zamknieta")
# Baza została podłączona
# Baza została zamknieta

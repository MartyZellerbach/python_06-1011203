# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
# nosal, sql
# w pythonie sqllite3 - baza sql w jednym pliku, również może być przechowyuwana w pamięci
import sqlite3

#
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # ZAPISANE W JEZYKU SQ:
    query = '''
    CREATE TABLE IF NOT EXISTS developers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''
    insert = '''
    INSERT INTO developers (id, name, email, salary) VALUES (4, 'Ania', 'a@o2.pl', 7000);
    '''
    cursor = sql_connection.cursor()  # obiekt który komunik się z nami a baza musi być
    print("Baza została podłączona")
    #    sql_connection.execute(query)
    sql_connection.execute(insert)
    sql_connection.commit()


except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych", e)
finally:  # wykonuje się zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

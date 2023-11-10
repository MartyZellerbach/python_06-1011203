# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza została podłączona")
    # CRUD -> C
    insert = '''
        INSERT INTO software (id, name, price) VALUES (2, 'Python', 200);
        '''
    # cursor.execute(insert) insert wykonujemy raz
    # sql_connection.commit()
    # CRUD -> R
    select = '''
    SELECT * FROM software WHERE id=1;'''
    # CRUD -> U
    update = '''
    UPDATE software SET price = 2000 WHERE id=1;
    '''
    # cursor.execute(update) # komentuje bo nie potrzebujemy drugi raz robic update
    # sql_connection.commit()

    delete = '''
    DELETE FROM software WHERE id=1;
    '''
    #cursor.execute(select)
    #cursor.execute(insert)
    #sql_connection.commit()
    #cursor.execute(delete)
    #sql_connection.commit()


    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 100.0) poniewaz jest duzo danych mozna selecta wykonać tak jak tutaj


except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych", e)
finally:  # wykonuje się zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
# Baza została podłączona
# Baza została zamknieta
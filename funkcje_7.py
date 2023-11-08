# x: str = 43
# print(x)


def connect(**opcje):
    print(opcje)  # {'a': 7}
    print(type(opcje))  # <class 'dict'>
    param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(param)  # {'host': '127.0.0.7', 'port': '8080'}
    param.update(opcje)
    print(param)  # {'host': '127.0.0.7', 'port': '8080', 'a': 7}
    param['pwd'] = opcje  # słownik jako wartość argumentu dla klucza pwd
    print(param)  # {'host': '127.0.0.7', 'port': '8080', 'a': 7, 'pwd': {'a': 7}}


def connect_all(*args, **kwargs):
    print(args, kwargs)


connect()  # {} słownik, a słownik to klucz i wartość
connect(a=7)  # argument nazwy
connect_all(1, 2, 3, 4, "Radek", "Zenek", a=8, b=9, c=9, name="radek")


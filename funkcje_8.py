def allparams(a, b, /, **kwargs):
    print(a)
    print(b)
    print(kwargs)


def allparams2(a, b, /, c):
    print(a, b, c)


def allparams3(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args, kwargs", args, kwargs)


allparams(1, 2)
allparams(1, 2, c=8)
# dodanie / do aregumentów powoduje że argumenty z lewej strony muszą być podane jako pozycyjne
# pozostałe wg reguł
# allparams(1, b=2, c=7)  # b - taka sama nazwa jak w def allparams, powinna iśc do kwargs a nie poszła wiec dodajemt /
allparams(1, 2, b=2, c=3)  # {'b': 2, 'c': 3}
allparams2(1, 2, 3)  # 1 2 3
allparams3(1, 2)
#gdy chcemy wrzuć wartości do args, c musimy podaj pozychnuie, nie można po nazwach używać
allparams3(1, 2, 67, 7, 8, 9)  # args, kwargs (7, 8, 9) {}
allparams3(1, 2, 67, 7, 8, 9, 11, 12, d=89)
allparams3(1, 2, 67, 7, 8, 9, 11, 12, args=89, kwargs=9, kwargs2=9)
allparams3(1, 2, 67, 7, 8, 9, 11, 12, args=89, kwargs=9, kwargs2=9)
allparams3(1, 2, a=0)  # trafi do kwargs, gdyby była warotśc podać a to trafi właśnie do kwargs a nie do a.

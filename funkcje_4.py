# funkcje zagnieżdżone
def fun1():
    print("To jest fun1")

    def fun2():  # deklaracja fun2
        print("To jest fun2")

    return fun2 # zwracamy tylko adres w pamięci gdziee jest umieszczona funkcja


print(fun1())  # wywołanie funkcji - To jest fun1 <function fun1.<locals>.fun2 at 0x0000026E71258A40>
print(type(fun1()))  # <class 'function'>
# przechowanie
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000026E71258A40>
xFun()

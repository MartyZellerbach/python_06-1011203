# match case - instrukcja sterowania przepływem programu
#
lista = []
lang = input("Podaj znany Ci język programowania: ")

match lang:
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _: # domyślne zachowania, odpowienik else
        print("Nie znam takiego języka")
print(lista)
print("Super! Znam ten język programowania który podałeś.")


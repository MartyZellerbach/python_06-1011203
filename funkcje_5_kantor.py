# utworzenie funkcji kantor
# kantor ma działać że mamy dwie osoby danego dnia
# dana osoba umie wymieniać tylko jeden tym waluty dolary/euro
# zrobić z wykorzystaniem funkcji wewnętrznych
# kantor
# dwie wewnętrzne funkcje (used, eur)

def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} dol = {kwota * 4.13} pln")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur = {kwota * 4.53} pln")

    if waluta.lower().replace(" ", "") == 'eur':
        return eur
    else:
        return usd

kantor_eur = kantor('eur')
kantor_eur(1000)  # Wymieniam euro
kantor_usd = kantor('usd')
kantor_usd(1000)


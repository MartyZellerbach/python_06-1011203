# decimal który zachowuje precyzhe przy obliczniach
# w odróżnieniu od float jest mniej narażony na błąd zaokrąglenia

from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')


print(kwota1, kwota2)  # 10.25 5.50
suma = kwota1 + kwota2
print("Suma", suma)

kwota3 = Decimal('0.7')
kwota4 = Decimal('0.2')  # Suma 15.75
print(kwota3 + kwota4)  # 0.9

precyzja = Decimal('0.00')

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja))


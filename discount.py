# sklep
from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-11-08
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-11-08 08:46:37.607712
print(type(time))  # <class 'datetime.datetime'>

tomm = today + timedelta(days=1)
print(tomm)  # 2023-11-09
print(type(tomm))  # <class 'datetime.date'>
print(time.hour)
print(today.day)

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 08/11/2023
print(datetime.now().timestamp())  # 1699430183.723363 od 1 stycznia 1970
timestamp = datetime.now().timestamp()
print(datetime.fromtimestamp(timestamp))  # 2023-11-08 08:58:59.016509

print(timestamp)

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 09:01
print(formated_time.removeprefix("0"))  # 9:01

formated_time2 = datetime.now().strftime('%H:%M %p')
print(formated_time2)  # 09:08 AM
print(formated_time2.removeprefix("0"))  # 9:08 AM

formated_time3 = datetime.now().strftime('%I:%M %p')
print(formated_time3)  # 09:08 AM
print(formated_time3.removeprefix("0"))  # 9:08 AM

# [] lista
# {} słownik
# typ danych 100.0 float
products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomm, 'price': 200.0},
    {'sku': 4, 'exp_date': today, 'price': 150.0}
]

print(products)
for product in products:
    # print(product)
    # if product['exp_date'] == today:
    #     product['price'] *= 0.8
    #     print(f"""
    #     Price for {product['sku']}
    #     is now {product['price']}""")
# ctrl + / - komentarz zaznaczonych linii
    if product['exp_date'] != today:
        continue  # kończy bieżącą iteracje pętli, wraca na początek pętli, pobiera koljny element
    product['price'] *= 0.8
    print(f"""
    Price for {product['sku']} 
    is now {product['price']}""")
    # Price for 1
    # is now 80.0
    #
    # Price for 2
    # is now 64.0
    #
    # Price for 4
    # is now 120.0





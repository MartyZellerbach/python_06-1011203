import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/CHF/'
response = re.get(url)
print(response)  # <Response [200]>
# 200 - OK

table = response.json()
print(table)
print(type(table))
print(table.keys())
print(table['table'])
print(table['currency'])
print(table['code'])  # [{'no': '216/A/NBP/2023', 'effectiveDate': '2023-11-08', 'mid': 4.6343}]
print(table['rates'][0])  # {'no': '216/A/NBP/2023', 'effectiveDate': '2023-11-08', 'mid': 4.6343}
print(table['rates'][0].keys())  # dict_keys(['no', 'effectiveDate', 'mid'])
for k, v in table['rates'][0].items():
    print(k, "=>", v)
rates = table['rates'][0]
print(table['rates'][0]['no'])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])  # 4.6343
print(rates['no'], rates['effectiveDate'], rates['mid'])  # 216/A/NBP/2023 2023-11-08 4.6343
# pobrać ceny złota
# pydantic

url = 'http://api.nbp.pl/api/cenyzlota/today'
response_gold = re.get(url)

table_gold = response_gold.json()
print(table_gold)
print(type(table_gold))
print(table_gold[0]['data'])
print(table_gold[0]['cena'])



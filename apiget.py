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
print(table['rates'][0]['mid'])
print(rates['no'],rates['effectiveDate'],rates['mid'])


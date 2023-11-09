import pandas as pd

data = pd.read_csv('records.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3   9.1
# 1  Tomek    cos     2   9.0
# 2  Zenek    cor     1   0.5
# 3  Zosia    coa     8   0.0
print(data.columns)
print(data.values)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
# [['radek' 'coe' 3 9.1]
#  ['Tomek' 'cos' 2 9.0]
#  ['Zenek' 'cor' 1 0.5]
#  ['Zosia' 'coa' 8 0.0]]
print(data.values[0])  # ['radek' 'coe' 3 9.1]
print(type(data.values))  # <class 'numpy.ndarray'>
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3   9.1
# 1  Tomek    cos     2   9.0
# 2  Zenek    cor     1   0.5
# 3  Zosia    coa     8   0.0>

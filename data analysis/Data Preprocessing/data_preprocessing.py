# import csv
#
# import pandas as pd
# x = pd.read_csv("/Users/Home/Desktop/df_nnz.csv")
# print(x)
# for line in x:
#     #вывод в одну строку названий шапок массива данных для рассмотрения
#     print(line[0::], end=' ')

import csv
with open("df_nnz.csv", "r") as f:
    reader = csv.DictReader(f)
    for line in reader:
        #тут вывод с ключом значения и словарем
        print(line, end='\n')


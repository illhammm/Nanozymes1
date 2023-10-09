import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("../Data Analysis/df_nnz.csv")

#функция меняет тип данных в float
def to_numeric_column(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df
df = to_numeric_column(df, 'Vmax')
df = to_numeric_column(df, 'Km')

#перевожу значения в читаемые значения
#print(df['Vmax'].describe())
df.loc[:, 'Vmax_log'] = np.log10(df['Vmax'])
#print(df['Vmax_log'].describe())

sns.boxplot(x=df['Vmax_log'])
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../Data_Analysis/df_nnz.csv")
def to_numeric_column(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df
df = to_numeric_column(df, 'Vmax')
df = to_numeric_column(df, 'Km')



df = df.dropna(subset=['Vmax', 'Km'], axis =0)
df_nan = df.isna().mean().sort_values(ascending = False)
#print(df_nan.head(10))

df_colums = ['ph','Complexity','temp']
nan_rows = df[df[df_colums].isnull().any(axis=1)]
# print(nan_rows[df_colums])
df = df.dropna(axis =0)
df_nan = df.isna().mean().sort_values(ascending = False)
# print(df_nan.head(10))


#print(df[df.duplicated ()])

df.loc[:, 'Vmax_log'] = np.log10(df['Vmax'])
sns.boxplot(x=df['Vmax_log'])
#plt.show()
#команда выводит boxplot

def counts_quantil(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((column < (Q1 - 1.5 * IQR)) | (column > (Q3 + 1.5 * IQR)))
    num_outliers = outliers.sum()
    filtered_data = column[~outliers]

    return num_outliers



def del_quantil(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    df = df[~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]

    return df

df = del_quantil(df, 'Km')
print(counts_quantil(df['Km']))
print(counts_quantil(df['Vmax_log']))
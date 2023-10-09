import pandas as pd
import numpy as np

df = pd.read_csv("../Data Analysis/df_nnz.csv")
def to_numeric_column(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df
df = to_numeric_column(df, 'Vmax')
df = to_numeric_column(df, 'Km')


print(df['Vmax'].describe())
df.loc[:, 'Vmax_log'] = np.log10(df['Vmax'])
print(df['Vmax_log'].describe())

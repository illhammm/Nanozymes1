import pandas as pd

df = pd.read_csv("../Data_Analysis/df_nnz.csv")
def to_numeric_column(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df
df = to_numeric_column(df, 'Vmax')
df = to_numeric_column(df, 'Km')

#print(df.dtypes)


df = df.dropna(subset=['Vmax', 'Km'], axis =0)
df_nan = df.isna().mean().sort_values(ascending = False)
print(df_nan.head(10))
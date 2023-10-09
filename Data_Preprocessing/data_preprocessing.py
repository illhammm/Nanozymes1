import pandas as pd

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
print(nan_rows[df_colums])
df = df.dropna(axis =0)
df_nan = df.isna().mean().sort_values(ascending = False)
print(df_nan.head(10))
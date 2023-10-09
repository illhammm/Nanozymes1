import pandas as pd
df = pd.read_csv("df_nnz.csv")
#print(df)

df_nan = df.isna().mean().sort_values(ascending = False)
#print(df_nan.head(10))

print(df.dtypes)
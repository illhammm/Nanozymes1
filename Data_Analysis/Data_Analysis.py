import pandas as pd
from Data_Preprocessing.data_preprocessing import to_numeric_column

df = pd.read_csv("df_nnz.csv")


df_nan = df.isna().mean().sort_values(ascending = False)


#print(df.dtypes)

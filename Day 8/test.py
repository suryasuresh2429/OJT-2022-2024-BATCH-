import pandas as pd
df=pd.read_csv('data.csv')
print(df)

df_cleaned_row=df.dropna(how='all')
df_cleaned_col=df_cleaned_row.dropna(axis=1,how='all')
print(df_cleaned_col)
print(df_cleaned_row)
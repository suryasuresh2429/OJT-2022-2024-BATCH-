import pandas as pd
data={
    "name":["anu","manu","malu"],
    "age":[25,31,24],
    "city":["banglore","chennai","hyderabad"]
}
df=pd.DataFrame(data)
print(df)
print(df[['name','city']])
print(df.loc[2])
print(df[df['age']>30])
df['stipend']=[5000,6000,4000]
print(df)
df=df.drop(columns=['age'])
print(df)

print(df.describe())

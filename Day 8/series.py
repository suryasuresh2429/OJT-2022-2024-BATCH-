import pandas as pd

dict={"name":"maya","age":24,"place":"Tvm"}
df=pd.Series(dict)
print(df)


data = [10,2,3,4,7]
series = pd.Series(data)
 
print(series)
 
print(series[3])
 
series_add = series + 5
 
print(series_add)
 
filtered_series = series[series > 10]
print(filtered_series)

mean = series.mean()
print (f"the mean value of the series is {mean}")
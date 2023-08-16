
import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-26/Desktop/data set/Iris.csv")
print(data)
print(data.head(5))
print(data.tail(5))
print(data["PetalLengthCm"])
print(data.count())
print(data.info())
print(data.dtypes)

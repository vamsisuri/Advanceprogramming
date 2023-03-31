import pandas as pd
import random
# data=[100,200,300,400,250]
# s=pd.Series(data,index=['a','b','c','d','e'])
# print(s)
# dates=pd.date_range(start='2023-02-01',end='2023-03-31',freq='W-SUN')
# print(dates)
# sd=pd.Series(dates)
#print(sd)
dates=pd.date_range(start='2023-02-01',end='2023-02-28')
temp=[random.randint(28,31) for i in range(1,29)]

day_temp=pd.Series(temp,dates)
print(day_temp.describe())

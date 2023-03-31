import pandas as pd
import random
temp={'Chenna':[random.randint(28,31) for i in range(1,10)],
      'Bangalore':[random.randint(27,30) for i in range(1,10)],
      'Vijayawada':[random.randint(27,30) for i in range(1,10)]}
humidity=[random.randint(30,35) for i in range(1,10)]
df=pd.DataFrame(temp)
df['humidity']=humidity
# df.drop('humidity',axis=1,inplace=True)
# #print(df.iloc[:,0])
# print(df)
# temp1=df.loc[df['Chennai']>28]
# print(temp1)
# rowdrop=df.drop(1,axis=0).reset_index(drop=True)
# print(rowdrop)
df.rename(columns={'Chenna':'Chennai'},inplace=True)
print(df)
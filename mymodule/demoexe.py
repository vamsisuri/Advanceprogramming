from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql+pymysql://Lava:Lava2233@localhost/myhcl'
db_connection = create_engine(db_connection_str)
df=pd.read_excel("c://mydataset//sample_pivot.xlsx",sheet_name='Sheet1',parse_dates=['Date'])
#east = df.where(df['Region']=='East')
#print(data)
cp=df.copy()
#print(df.isna().sum())
# df.fillna('mean',inplace=True)
# print(df.isna().sum())
print(df.sort_values(['Region'],ascending=False))
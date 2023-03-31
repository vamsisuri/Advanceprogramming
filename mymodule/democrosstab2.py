import pandas as pd
from sqlalchemy import create_engine
# import pandas as pd

db_connection_str = 'mysql+pymysql://Lava:Lava2233@localhost/myhcl'
db_connection = create_engine(db_connection_str)
df=pd.read_excel("c://mydataset//sample_pivot.xlsx",sheet_name='Sheet1',parse_dates=['Date'])
# task1=pd.crosstab(index=df['region'],columns=df['Type'],values=df['Sales'],aggfunc='mean'
# task2 = pd.crosstab([df.Region,df.Date.dt.quarter],df.Type,values=df.Sales,margins=True,aggfunc='sum')
task3 = pd.crosstab([df.Region,df.Date.dt.quarter],df.Type,values=df.Sales,margins=True,aggfunc='sum')
df.to_sql(name='task3', con=db_connection)
print(task3)



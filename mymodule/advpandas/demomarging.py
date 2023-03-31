from functools import reduce
from sqlalchemy import create_engine



db_connection_str="mysql+pymysql://Lava:Lava2000@localhost/myhcl"
db_connection=create_engine(db_connection_str)
list = []
sheet_names = ['jan','feb','march','apirl','may','june','july','aug','sep','oct','nov','dec']
for k in sheet_names:
    df = pd.read_excel("C://mydataset//merging.xlsx", sheet_name=k)
    list.append(df)
di=pd.read_excel("C://mydataset//merging.xlsx", sheet_name=sheet_names)
data=reduce(lambda left,right:pd.merge(left,right,on='Product_id',how='inner'),l)
try:
    di.to_sql(name="mytabel1",con=db_connection)
except Exception as e:
    print(e)
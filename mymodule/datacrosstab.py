import pandas as pd
customers=pd.read_excel("C://mydataset//hcl_order.xlsx",sheet_name="Customers")
orders=pd.read_excel("C://mydataset//hcl_order.xlsx",parse_dates=["order_date"],sheet_name="Orders")
products=pd.read_excel("C://mydataset//hcl_order.xlsx",sheet_name="products")
result=pd.merge(left=customers,right=orders,on="cust_id",how='inner')
res=customers.merge(orders,on="cust_id").merge(products,on="Order_id")
#print(result)
r=pd.concat([customers,orders],axis=1)
print(r)


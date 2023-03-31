import mysql.connector
from  mysqlconnection import Crud_operations
class Crud_operation(Crud_operations):
    def __init__(self):
        super().__init__("localhost", "root", "Lava@2000", "myhcl", 3306)
        self.cur=self.connection.cursor()

    def Insertdata(self,data):
        self.data=data
        sql = "Insert into file values(%s,%s,%s,%s):"
        self.cur.excute(sql, (data,))
        self.connection.commit()
        print("Data inserted successfully")
    def delete(self,data):
        self.data=data
        sql= "delete from tablename where prod_id=(%s)"
        self.cur.execute(sql, (data,))
        self.connection.commit()
        print("Data deleted successfully")
    def selectrecord(self,data):
        self.data = data
        sql="select * from tablename"
        self.cur.execute(sql, (data),)
        self.connection.commit()
        print("selected")
    def update(self,data):
        sql="update tablename set prod_price=(%s) where prod_id=(%s)"
        self.cur.execute(sql, (data,))
        print("updated successfully")
try:
    obj=Crud_operation()
    print(obj.connection.is_connected())
except Exception as e:
    print(e)














    
    

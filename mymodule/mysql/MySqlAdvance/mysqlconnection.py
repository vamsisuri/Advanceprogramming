import mysql.connector


class Crud_operations():
    def __init__(self,host,username,password,database,port):
            self.hostname=host
            self.username=username
            self.password=password
            self.database=database
            self.portnum=port
            self.connection=mysql.connector.connect(host=self.hostname,username=self.username,password=self.password,database=self.database,port=self.portnum)
        # self.cur=self.connection.cursor()
try:
    obj = Crud_operations("localhost", "root", "Lava@2000", "myhcl", 3306)
except Exception as e:
    print(e)



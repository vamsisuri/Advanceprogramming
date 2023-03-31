from mysql  import Crud_operations
obj=Crud_operations()
def insertdata():
    name=input("Enter the name")
    age=int(input("Enter the age"))
    place=input("Enter the place")
    data=(name,age,place)
    obj.insert(data)
def deletedata():
    name=input("enter the name")
    data=(name)
    obj.delete(data)
def selectdata():
    print(obj.selectrecord())
def updatedata():
    name=input("enter the name")
    age=int(input("enter the age"))
    data=(name,age)
    obj.update(data)
def Userinterface():
    while(True):
        print("1.Insert data")
        print("2.Delete data")
        print("3.Select Record")
        print("4.Update record")
        print("5.create record")
        print("6.exit")
        choice=int(input("Enter your choice"))
        if choice==1:
            insertdata()
        elif choice==2:
            deletedata()
        elif choice==3:
            selectdata()
        elif choice==4:
            updatedata()
        elif choice==5:
            obj.create_table()
        else:
            exit()
        break
Userinterface()



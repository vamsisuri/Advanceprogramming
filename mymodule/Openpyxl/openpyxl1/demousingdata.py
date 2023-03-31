import openpyxl as xl
from dataclasses import dataclass

@dataclass
class Person:
    name : str
    contact : int
    email : str
    location : str
wb=xl.Workbook()
ws=wb.active
persons=[
        Person(name="Vamsi",contact=167234,email='lavakumar@22345678',location='bangalore'),
        Person(name="Vamsi", contact=167234, email='lavakumar@22345678', location='chennai'),
        Person(name="Vamsisuri", contact=167234, email='lavakumar@22345678', location='bhutan'),
]
data=[[p.name,p.contact,p.email,p.location]for p in persons]
mydata=[['Name','Contact','Email','Location']]+data
print(mydata)
for row in mydata:
    ws.append(row)
wb.save("C://mydataset//dataclass.xlsx")

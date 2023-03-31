import openpyxl as xl
from openpyxl import Workbook
from openpyxl.workbook import Workbook

rows = [
    ["Products", "Online", "Store"],
    [1,30,45],
    [2,40,30],
    [3,40,25],
    [4,50,30],
    [5,30,25],
    [6,25,36],
    [7,20,40],
]
wb=Workbook()
sh=wb.active
for row in rows:
    sh.append(row)
    wb.save("C://mydataset//mysheet.xlsx")



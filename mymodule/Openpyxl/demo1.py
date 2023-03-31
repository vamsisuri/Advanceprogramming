import openpyxl as xl
from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference
workbook=Workbook()
sheet=workbook.active
rows = [
    ["Products", "Online", "Store"],
    [1, 30, 45],
    [2, 40, 30],
    [3, 40, 25],
    [4, 50, 30],
    [5, 30, 25],
    [6, 25, 36],
    [7, 20, 40],
    ]
for row in rows:
    sheet.append(row)
chart1 = BarChart()
data1 = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=8,
                 min_col=2,
                 max_col=3)

chart1.add_data(data1, titles_from_data=True)
sheet.add_chart(chart1,"E2")
workbook.save("C://mydataset//sheet3.xlsx")

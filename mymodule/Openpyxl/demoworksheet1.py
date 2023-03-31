from openpyxl import Workbook
from openpyxl.chart import BarChart,LineChart,Reference
import openpyxl as xl

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
chart = BarChart()
data = Reference(Worksheet=sheet,
                 min_row=1,
                 max_row=3,
                 min_col=2,
                 max_col=3)

chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart,"E2")
workbook.save("C://mydataset//sheet1.xlsx")

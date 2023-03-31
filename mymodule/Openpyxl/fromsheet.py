import openpyxl as xl
from openpyxl.styles import Font,Alignment
wb=xl.load_workbook("C://mydataset//mysheet.xlsx")
sh=wb.active
font=Font(bold=True,size=20)
alignmt=Alignment(horizontal='center')
sh['A1'].font=font
sh['A1'].alignment=alignmt
wb.save("C://mydataset//mysheet.xlsx")

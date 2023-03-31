import openpyxl as xl
wb=xl.load_workbook("C://mydataset//studentdata.xlsx")
sheet=wb['Sheet3']
list=[]

for i in range(1,4):
    list1=[]
    #list1.clear()
    for j in range(1,4):
        #list2.clear()
        list1.append(sheet.cell(j,i).value)
    list.append(list1)
print(list)


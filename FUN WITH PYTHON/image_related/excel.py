import xlsxwriter
outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

NAME = ["NAMES","ABHAY KUMAR","DENNY H KONYAK","ANJANA","BEN"]
BRANCH = ["SALARY",10000,10000,200000,300000]

for i  in range(len(NAME)):
    outSheet.write(i,10,NAME[i])
    outSheet.write(i,11,BRANCH[i])
outWorkbook.close ()
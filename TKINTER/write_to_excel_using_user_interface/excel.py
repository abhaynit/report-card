from tkinter import *
import xlsxwriter
from xlsxwriter.worksheet import Worksheet
outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()


f=open("student.txt",'r')
s=f.read()

import json
data = json.loads(s)
root = Tk()

la1 = Label(root,text="NAME : ")
la1.place(x=10,y=10)

en1 = Entry(root)
en1.place(x=100,y=10)

la2 = Label(root,text="BRANCH : ")
la2.place(x=10,y=30)

en2 = Entry(root)
en2.place(x=100,y=30)

la3 = Label(root,text="REG_NO : ")
la3.place(x=10,y=50)

en3 = Entry(root)
en3.place(x=100,y=50)

la4 = Label(root,text="SEM : ")
la4.place(x=10,y=70)

en4 = Entry(root)
en4.place(x=100,y=70)

tex = StringVar()
tex.set(" ")
def result():
    ke = len(data)
    print(ke)
    name = en1.get()
    branch = en2.get()
    reg = en3.get()
    sem = en4.get()
    data[ke+1]= [name,branch,reg,sem]
    book= dict(data)
    import json
    s = json.dumps(book)
    print(s)
    with open('student.txt','w') as f:
        f.write(s)
    
    


def prin():
    f=open("student.txt",'r')
    s=f.read()
    data = json.loads(s)
    for i  in  data.items():
        for j in range(len(i[1])):
            outSheet.write(int(i[0])-1,j,i[1][j])
    outWorkbook.close()

submit = Button(root,text = "SUBMIT",command=result)
submit.place(x=100,y=100)
generate = Button(root,text = "PRINT",command=prin)
generate.place(x=100,y=150)

root.mainloop()
from tkinter import *
from tkinter.font import BOLD 
from tkinter.ttk import *
import datetime
from time import strftime

window = Tk()
window.title('abhay kumar')
window.minsize(width=1200,height=310)

result1 = Label(window,font=('verdana',10),background="skyblue",foreground="brown")
result1.place(x=850,y=50)

t1 = datetime.datetime.now()
qw = "TODAYS DATE IS    : " +str(t1.strftime("%A")).upper()+" " +str(t1.strftime("%d")).upper() +"  " + str(t1.strftime("%B")).upper()
result1.configure(text = qw)

Label(window,text="LOGIN FORM",background="green",foreground="white", font=('verdana',20,BOLD)).pack()

Label(window,text="SELECT THE SEMESTER  : ",background="pink",font=('verdana',10,BOLD)).place(x=200,y=100)


n = StringVar()
name = StringVar()
name_help =StringVar()
name_help.set("enter name")
pas = StringVar()
pas_help = StringVar()
pas_help.set("enter password")

def ref():
    Entry(window,textvariable=name,width=27  ).place(x=410,y=150)
    Entry(window,textvariable=pas, width=27, show='*').place(x=410,y=200)
    Button(window,text='submit',command=abhi).place(x= 600,y=250)

def destrouy():
    window.destroy()



def abhi():
    print("SEM  :",n.get())
    print("NAME : ",name.get())
    print("PASS : ",pas.get())

    t = datetime.datetime.now()
    qw = "YOUR RESPONSE HAS BEEN SUBMITTED THE CURRENT TIME IS  : " + str(t.hour)+ " : "+str(t.minute) + " : "+str(t.second)
    result.configure(text = qw)
    
    name.set("")
    pas.set("")

    Entry(window,textvariable=name,width=27  ,state=DISABLED ).place(x=410,y=150)
    Entry(window,textvariable=pas, width=27, show='*',state= DISABLED).place(x=410,y=200)
    Button(window,text='submit',command=abhi, state=DISABLED).place(x= 600,y=250)

    result.after(10000,destrouy)
    





month = Combobox(window,width=27,textvariable=n,background="pink")


month['values'] = (
                    '1st','2nd','3rd','4th','5th','6th','7th','8th'
)

month.place(x=410,y=100)
month.current(0)

Label(window,text='ENTER YOUR NAME : ',background="yellow",font=('verdana',10,BOLD)).place(x=200,y=150)

Label(window,text='ENTER YOUR PASSWORD : ',background="yellow",font=('verdana',10,BOLD)).place(x=200,y=200)

Entry(window,textvariable=name,width=27).place(x=410,y=150)

#Entry(window,textvariable=name_help,state=DISABLED,  width=27).place(x=600,y=150)
Entry(window,textvariable=pas, width=27, show='*').place(x=410,y=200)

#Entry(window,textvariable=pas_help,  state=DISABLED, width=27).place(x=600,y=200)

Button(window,text='submit',command=abhi).place(x= 600,y=250)

Button(window,text='submit other response',command=ref).place(x= 800,y=250)

result = Label(window)
result.place(x=100,y=274)

#window.resizable(0,0)



def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000,time)


lbl = Label(window,font=('calibri',20,'bold',),foreground='black')
lbl.place(x=10,y=30)
time()


window.mainloop()


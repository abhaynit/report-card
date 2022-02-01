# Import Required Library
from cProfile import label
from tkinter import *
import tkinter as tk
from tkinter import Button, ttk
from tkcalendar import Calendar

def call_fun():
# Create Object
    root = Tk() 

    # Set geometry
    root.geometry("600x380")

    Label(root, text = "REGISTRATION WINDOW",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).pack()
    Label(root, text = "Registration No",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=60)
    Label(root, text = "Name",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=110)
    Label(root, text = "Branch",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=160)
    Label(root, text = "Date of Birth ",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=210)
    Label(root, text = "(dd/mm/yyyy) ",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=400,y=210)
    Label(root, text = "Gender",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=260)


    reg_no = StringVar()
    name = StringVar()
    Entry(root,textvariable = reg_no,width=50, font=('calibre',10,'normal')).place(x=200,y=60)
    Entry(root,textvariable = name,width=50, font=('calibre',10,'normal')).place(x=200,y=110)

    n1 = StringVar()
    branch = ttk.Combobox(root, width = 50, textvariable = n1)

    # Adding combobox drop down list
    branch['values'] = ('computer science and engineering','electrical and instrumentation engineering',
                        'electrical and electronics engineering','civil engineering','mechanical engineering',
                        'electronics and communication enginering'
                        )

    branch.place(x=200,y=160)

    #day
    da = StringVar()
    day = ttk.Combobox(root, width = 5, textvariable = da)

    # Adding combobox drop down list
    day_value = []
    for i in range(31):
        day_value.append(i+1)
    day['values'] = tuple(day_value)
    day.place(x=200,y=210)

    #month
    mo = StringVar()
    month = ttk.Combobox(root, width = 5, textvariable = mo)

    # Adding combobox drop down list
    month_val = []
    for i in range(12):
        month_val.append(i+1)
    month['values'] = tuple(month_val)
    month.place(x=250,y=210)

    yea = StringVar()
    year = ttk.Combobox(root, width = 5, textvariable = yea)

    # Adding combobox drop down list
    yer_val  =[]
    for i in range(50):
        yer_val.append(1980+i)
    year['values'] = tuple(yer_val)
    year.place(x=300,y=210)

    gen = StringVar()
    gender = ttk.Combobox(root, width = 5, textvariable = gen)

    # Adding combobox drop down list
    gender['values'] = ('M','F')
    gender.place(x=200,y=260)


    def select():
        from student_registration import registration
        dob = yea.get()+'-'+mo.get()+'-'+da.get()
        if registration(reg_no.get(),name.get(),gen.get(),dob,branch.get()):
            Label(root, text = "INSERTED SUCCESSFULLY".center(30,'*'),	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=200,y=330)
        else:
            Label(root, text = "ERROR IN SOME DATA".center(30,'*'),	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=200,y=330)
    Button(root, text = "REGISTER",command = select).place(x=200,y=300)


    # Execute Tkinter
    root.resizable(0,0)
    root.mainloop()
call_fun()
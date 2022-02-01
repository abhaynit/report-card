# Import Required Library
from tkinter import *
import tkinter as tk
from tkinter import Button, ttk
from matplotlib.pyplot import subplots_adjust
from sympy import im
from tkcalendar import Calendar


def call_fun():
# Create Object
    root = Tk()

    # Set geometry
    root.geometry("500x200")

    Label(root, text = "DELETE STUDNET WINDOW",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).pack()
    Label(root, text = "Registration No",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=60)

    reg_no = StringVar()
    regn = ttk.Combobox(root, width = 25, textvariable = reg_no)
    import mysql.connector
    conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
    cur_obj = conn.cursor()
    cur_obj.execute('use result')
    query1 = 'select reg_no from student_detail'
    cur_obj.execute(query1)
    regno = []
    for i in cur_obj:
        regno.append(i[0])
    regn['values'] = tuple(regno)
    regn.place(x=200,y=60)

    def delete_data():
        from student_registration import delete_registration
        if delete_registration(reg_no.get()):
            Label(root, text = "DELETED SUCCESSFULLY".center(30,'*'),	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=80,y=130)
        else:
            Label(root, text = "FAILED TO DELETE".center(30,'*'),	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=80,y=130)
        import time 
        #time.sleep(5)
        root.destroy()
        call_fun()
    Button(root, text = "GO".center(20,' '),command = delete_data).place(x=240,y=110)


    # Execute Tkinter
    root.resizable(0,0)
    root.mainloop()
call_fun()

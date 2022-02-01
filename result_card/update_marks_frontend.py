# Import Required Library
from tkinter import *
import tkinter as tk
from tkinter import Button, ttk
from turtle import update
from matplotlib.pyplot import subplots_adjust
from tkcalendar import Calendar

    # Create Object
def call_fun():
    root = Tk()

    # Set geometry
    root.geometry("600x500")

    Label(root, text = "MARKS UPDATION WINDOW",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).pack()
    Label(root, text = "Registration No",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=60)
    Label(root, text = "sem",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=110)
    #Label(root, text = "date of exam",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=10,y=160)



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

    se = StringVar()
    sem = ttk.Combobox(root, width = 15, textvariable = se)
    # Adding combobox drop down list
    sem['values'] = ('1','2','3','4','5','6','7','8')
    sem.place(x=200,y=110)

    bra = tk.StringVar()
    branch = ttk.Combobox(root, width = 15, textvariable = bra)
    branch['values'] = ('cse','eie','eee','ece','me','ce')
    branch.place(x=350,y=110)

    sub1 = StringVar()
    sub2 = StringVar()
    sub3 = StringVar()
    sub4 = StringVar()
    sub5 = StringVar()
    sub6 = StringVar()
    sub7 = StringVar()
    sub8 = StringVar()
    sub9 = StringVar()

    abc = [sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9]

    """
    mo = StringVar()
    month = ttk.Combobox(root, width = 5, textvariable = mo)
    month['values'] = ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')
    month.place(x=200,y=160)

    yea = StringVar()
    year = ttk.Combobox(root, width = 5, textvariable = yea)

    # Adding combobox drop down list
    yer_val  =[]
    for i in range(50):
        yer_val.append(1980+i)
    year['values'] = tuple(yer_val)
    year.place(x=280,y=160)

    """
    def subject_list(): 
        #data from database
        import mysql.connector
        conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
        cur_obj = conn.cursor()
        cur_obj.execute('use result')


        query1 = 'select sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9 from marks where reg_no = %s and semester = %s'
        cur_obj.execute(query1,(int(reg_no.get()),int(sem.get())))
        grade_list_value = []
        for i in cur_obj:
            for k in i:
                grade_list_value.append(k)

        #data from json format


        import json
        f = open('abc.txt','r')
        s = f.read()
        book = json.loads(s)
        final_value = book[str(bra.get())]['sem'+str(se.get())]
        y_vaL = 210
        x_val = 10
        count =0
        faltu = 0
        for i in final_value:
            if count==3:
                y_vaL+=50
                x_val=10
                count=0
            Label(root, text = str(i[0]),	background = 'green', foreground ="white",font = ("Times New Roman", 11)).place(x=x_val,y=y_vaL)
            grade = ttk.Combobox(root, width = 5, textvariable = abc[faltu] )
            grade['values'] = ('S','A','B','C','D','E','F','U','AB')
            grade.place(x=x_val+70,y=y_vaL)
            grade_list1 = ['S','A','B','C','D','E','F','U','AB']
            kqw = grade_list1.index(grade_list_value[faltu].upper())
            faltu+=1
            grade.current(kqw)
            x_val+=190 
            count+=1
        Button(root, text = "GO".center(20,' '),state=DISABLED, command = subject_list).place(x=240,y=160)
        
        def update_another():
            root.destroy()
            call_fun()
        def select():
            from student_registration import marks_updation

            if marks_updation(reg_no.get(),se.get(),sub1.get(),sub2.get(),sub3.get(),sub4.get(),sub5.get(),sub6.get(),sub7.get(),sub8.get(),sub9.get()):
                Label(root, text = "ADDED SUCCESFULLY".center(30,'*'),	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=200,y=y_vaL+100)
            else:
                Label(root, text = "FAILED TO ADD".center(30,'*'),	background = 'green', foreground ="white",font = ("Times New Roman", 15)).place(x=200,y=y_vaL+100)


        Button(root, text = "UPDATE".center(20,' '),command = select).place(x=200,y=y_vaL+50)
        Button(root, text = "UPDATE ANOTHER".center(20,' '),command = update_another).place(x=300,y=y_vaL+50)
    Button(root, text = "GO".center(20,' '),command = subject_list).place(x=240,y=160)


    # Execute Tkinter
    root.resizable(0,0)
    root.mainloop()

call_fun()

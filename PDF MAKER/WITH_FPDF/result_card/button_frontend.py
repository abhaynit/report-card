from re import sub
from subprocess import call
import tkinter as tk
from tkinter import Button, ttk
from unicodedata import name

import psutil
from sympy import im

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

def update_marks():
    from update_marks_frontend import call_fun
    call_fun()
def delete_student():
    from delete_student_frontend import call_fun
    call_fun()
def register_student():
    from registration_frontend import call_fun
    call_fun()
def result():
    from result_frontend import call_fun
    ak = call_fun()
    ak.abcd()

Button(window,text = 'UPDATE MARKS'.center(20,' '),command=update_marks).place(x=200,y=70)
Button(window,text = 'DELETE STUDENT'.center(20,' '),command=delete_student).place(x=200,y=110)
Button(window,text = 'REGISTER STUDENT'.center(20,' '),command=register_student).place(x=200,y=150)
Button(window,text = 'PRINT RESULT'.center(20,' '),command=result).place(x=200,y=190)
window.resizable(0,0)
window.mainloop()

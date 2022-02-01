import tkinter as tk
from tkinter import mainloop, ttk
from tkinter.font import BOLD

window = tk.Tk()
window.title('abhay kumar')

ttk.Label(window,text="COMBOBOXWIDGET",background="green",foreground="white", font=('verdana',20,BOLD)).place(x=600,y=0)

ttk.Label(window,text="SELECT FROM  THE OPTION : ",background="pink",font=('verdana',10,BOLD)).place(x=200,y=100)

n=tk.StringVar()

def abhi():
    print(n.get())

month = ttk.Combobox(window,width=27,textvariable=n,background="pink")

month['values'] = (
                    'JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER'
)

month.place(x=410,y=100)
month.current(0)

btn = ttk.Button(window,text='submit',command=abhi)

btn.place(x= 600,y=100)


window.mainloop()


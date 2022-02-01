from tkinter import *
from tkinter.font import BOLD 
from tkinter.ttk import *
import datetime
from time import strftime

window = Tk()
window.title('ABHAY KUMAR')
window.minsize(width=600,height=310)
ip_addr = StringVar()
ip_addr1 = StringVar()


def abhi():
    print("PASS : ",ip_addr.get())    
    
Label(window,text='select ip address : ',background="yellow",font=('verdana',10,BOLD)).place(x=100,y=150)
Entry(window,textvariable=ip_addr, width=50).place(x=270,y=150)

Button(window,text='submit',command=abhi).place(x= 300,y=250)
window.mainloop()
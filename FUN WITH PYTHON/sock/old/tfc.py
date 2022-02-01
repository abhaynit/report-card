from tkinter import *
from tkinter.font import BOLD 
from tkinter.ttk import *
import datetime
from time import strftime

window = Tk()
window.title('ABHAY KUMAR')
window.minsize(width=600,height=310)
Label(window,text="FILE TRANSFER",background="green",foreground="white", font=('verdana',20,BOLD)).pack()
pas = StringVar()
IP_ADDR = StringVar()

Label(window,text='IP ADDRESS : ',background="yellow",font=('verdana',10,BOLD)).place(x=100,y=200)
Entry(window,textvariable=IP_ADDR, width=50).place(x=270,y=200)

def abhi():
    import socket			
    s = socket.socket()		
    port = 12345
    ww = IP_ADDR.get()			
    s.connect((ww, port))
    file_location = pas.get()
    print("SERVER : ",s.recv(10000000).decode())
    s.send(file_location.encode())

    with open(file_location, "rb") as f:
        while True:
            byte = f.read(10000000)
            if not byte:
                s.send(''.encode())
                break
            s.send(byte)
            s.recv(10000000).decode()

    Button(window,text='submit',command=abhi, state=DISABLED).place(x= 300,y=250)
    
Label(window,text='ENTER FILE LOCATION : ',background="yellow",font=('verdana',10,BOLD)).place(x=100,y=150)
Entry(window,textvariable=pas, width=50).place(x=270,y=150)

Button(window,text='submit',command=abhi).place(x= 300,y=250)

result = Label(window)
result.place(x=100,y=274)
window.mainloop()
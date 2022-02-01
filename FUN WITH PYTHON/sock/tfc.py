from tkinter import *
from tkinter.font import BOLD 
from tkinter.ttk import *
import datetime
from time import strftime
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    print(filename)
window = Tk()
window.title('ABHAY KUMAR')
window.minsize(width=600,height=310)
Label(window,text="FILE TRANSFER",background="green",foreground="white", font=('verdana',20,BOLD)).pack()
pas = StringVar()
IP_ADDR = StringVar()

Label(window,text='IP ADDRESS : ',background="yellow",font=('verdana',10,BOLD)).place(x=100,y=200)
Entry(window,textvariable=IP_ADDR, width=50).place(x=270,y=200)

button_explore = Button(window,text = "Browse Files",command = browseFiles)
button_explore.place(x=100,y=250)

def abhi():
    import socket	
    s = socket.socket()		
    port = 12345
    ww = IP_ADDR.get()			
    s.connect((ww, port))
    print("SERVER : ",s.recv(1024).decode())
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_location = filename
    print(file_location)
    s.send(file_location.encode())

    with open(file_location, "rb") as f:
        while True:
            byte = f.read(1024)
            if not byte:
                s.send(''.encode())
                break
            s.send(byte)
            s.recv(1024).decode()

    Button(window,text='submit',command=abhi, state=DISABLED).place(x= 300,y=250)
    
Label(window,text='ENTER FILE LOCATION : ',background="yellow",font=('verdana',10,BOLD)).place(x=100,y=150)
Entry(window,textvariable=pas, width=50).place(x=270,y=150)

Button(window,text='submit',command=abhi).place(x= 300,y=250)

result = Label(window)
result.place(x=100,y=274)
window.mainloop()
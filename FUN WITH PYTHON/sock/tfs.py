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

def abhi():
    import socket	
    import os 		
    s = socket.socket()		
    print ("Socket successfully created")
    port = 12345			
    s.bind(('', port))		
    print ("socket binded to %s" %(port))
    s.listen(5)	
    print ("socket is listening")	

    c, addr = s.accept()	
    print ('Got connection from', addr )
    c.send('Connection established '.encode())

    qq = c.recv(1024).decode().split('/')[-1]
    print(qq)
    
    path_to_dir = 'E:\\ABHAY\\ABHAY_CREATIVITY\\shared_file'
    if os.path.exists(path_to_dir):
        pass
    else:
        os.makedirs(path_to_dir)
    saved_location = 'E:\ABHAY\ABHAY_CREATIVITY\shared_file'+'\\'+qq

    f2 = open(saved_location,'ab')
    while True:
        f2.write(c.recv(1024))
        c.send('ab'.encode())
    

Button(window,text='START_SERVER',command=abhi).place(x=250,y=150)

result = Label(window)
result.place(x=100,y=274)
window.mainloop()
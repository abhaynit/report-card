from tkinter import *
from tkinter.font import BOLD 
from tkinter.ttk import *
import socket	
from tkinter import filedialog		

# Creating tkinter window
window = Tk()
window.title('Combobox')
window.geometry('500x250')

# label text for title
Label(window, text = "FILE TRANSFER IN GB",background = 'green', foreground ="white",font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# label
Label(window, text = "Select the ip address",font = ("Times New Roman", 10)).grid(column = 0,row = 5, padx = 10, pady = 25)

# Combobox creation
n = StringVar()
monthchoosen = Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (
                        '127.0.0.1',
                        )

f1 = open('abh.txt','r')
bc = f1.read()
for i in bc.split(','):
    if i not in monthchoosen['values']:
        monthchoosen['values'] += (i,)
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()

def fetch_ip():
    print(n.get())
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("all files","*.*"),("Text files","*.txt*")))
    print(filename)
    send_file_name = (filename.split('/')[-1])

    s = socket.socket()		
    port = 12345	 
    ip_address = n.get()		
    s.connect((ip_address, port))

    file_location = filename
    print("SERVER : ",s.recv(10000000).decode())
    s.send(send_file_name.encode())
    print('sending the file named : ',send_file_name)

    with open(file_location, "rb") as f:
        while True:
            byte = f.read(10000000)
            if not byte:
                s.send(''.encode())
                print('file sent successfully')
                break
            s.send(byte)
            s.recv(10000000).decode() 

Button(window,text='SUBMIT',command=fetch_ip).place(x=200,y=100)
window.mainloop()

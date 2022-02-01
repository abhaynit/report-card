from tkinter import *
from tkinter.font import BOLD 
from tkinter.ttk import *
import socket	
import os 

# Creating tkinter window
window = Tk()
window.title('Combobox')
window.geometry('500x250')

# label text for title
Label(window, text = "SERVER WINDOW",background = 'green', foreground ="white",font = ("Times New Roman", 15)).pack()


window.destroy()

window.mainloop()
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

#*****************************************************************************************************

qq = c.recv(1024).decode().split('\\')[-1]
print('the file name is ',qq)
file_path = 'C:\ABHAY\FUN WITH PYTHON\shared_file'
#*****************************************************************************************************
if os.path.exists(file_path):
    pass
else:
    os.makedirs(file_path)
saved_location = file_path+'\\'+qq

f2 = open(saved_location,'ab')
while True:
    f2.write(c.recv(10000000))
    c.send('ab'.encode())

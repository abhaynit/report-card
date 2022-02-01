# python program demonstrating
# Combobox widget using tkinter


from tkinter import *
from tkinter.font import BOLD 
from tkinter.ttk import *

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
                        '127.0.0.2',
                        )

monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()

def fetch_ip():
    print(n.get())

Button(window,text='SUBMIT',command=fetch_ip).place(x=200,y=100)
window.mainloop()

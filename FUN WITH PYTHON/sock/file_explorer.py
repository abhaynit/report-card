from tkinter import *
from tkinter import filedialog

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))

button_explore = Button(window,text = "Browse Files",command = browseFiles)
import tkinter as tk
from tkinter import Button, ttk

# Creating tkinter window

window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

# label text for title
ttk.Label(window, text = "RESULT WINDOW",	background = 'green', foreground ="white",font = ("Times New Roman", 15)).pack()

# label
ttk.Label(window, text = "Select the semester :",font = ("Times New Roman", 15)).place(x=10,y=50)
ttk.Label(window, text = "Select the branch :",font = ("Times New Roman", 15)).place(x=10,y=100)
ttk.Label(window, text = "Select the reg_no :",font = ("Times New Roman", 15)).place(x=10,y=150)

# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 25, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = ('1','2','3','4','5','6','7','8')

monthchoosen.place(x=200,y=50) 
monthchoosen.current()

n1 = tk.StringVar()
monthchoosen1 = ttk.Combobox(window, width = 25, textvariable = n1)

# Adding combobox drop down list
monthchoosen1['values'] = ('cse','eie','eee','ece','me','ce')

monthchoosen1.place(x=200,y=100)
monthchoosen1.current()

name_var=tk.StringVar()
regn = ttk.Combobox(window, width = 25, textvariable = name_var)
import mysql.connector
conn = mysql.connector.connect(user = 'root',password ='abhaykumar')
cur_obj = conn.cursor()
cur_obj.execute('use result')
query1 = 'select reg_no from student_detail'
cur_obj.execute(query1)
regno = []
for i in cur_obj:
    regno.append(i[0])
regn['values'] = tuple(regno)
regn.place(x=200,y=150)

def find_value():
    print(n.get())
    print(n1.get())
    print(name_var.get(),n.get(),n1.get())
    from fee_receipt import print_result
    print_result(name_var.get(),n.get(),n1.get())
    import subprocess
    subprocess.Popen(['E:/old\old e drive/ABHAY/PDF MAKER/WITH_FPDF/result.pdf'],shell= True)
    #os.system("taskkill /f /im Acrobat.exe")
    """
    for p in psutil.process_iter():
        if p.name == '"C:/Program Files/Adobe/Acrobat DC/Acrobat/Acrobat.exe"':
            p.kill()
    """
    #subprocess.Pclose(['E:/old\old e drive/ABHAY/PDF MAKER/WITH_FPDF/result.pdf'],shell= True)
Button(window,text = 'PRINT RESULT'.center(20,' '),command=find_value).place(x=200,y=190)
window.resizable(0,0)
window.mainloop()
#call_fun()

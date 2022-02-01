from tkinter import * 
from tkinter.font import BOLD 
from tkinter.ttk import *
import pafy

window = Tk()
window.title('ABHAY KUMAR')
window.minsize(width=500,height=300)
n = StringVar()
url1 = StringVar()
def video():

    try:
        result1.configure(text = 'PLEASE WAIT')
        url = url1.get()
        available_format = n.get()
        video = pafy.new(url)
        best = video.getbest(preftype =available_format)
        result1.configure(text='DOWNLOAD STARTED')
        
        best.download()
        result1.configure(text = 'DOWNLOAD COMPLETE')
    except:
         result1.configure(text = 'NOT VALID FORMAT AVAILABLE')


Button(window,text='Download',command=video).place(x= 230,y=160)

result1 = Label(window,font=('verdana',10),background="skyblue",foreground="brown")
result1.place(x=250,y=200)
Label(window,text="YOU TUBE VIDEO DOWNLOAD",background="#16E2F5",foreground="#806517", font=('verdana',20,BOLD)).place(x=18,y=10)
Label(window,text='ENTER URL : ',background='#2B1B17',foreground='white',font=('verdana',13,BOLD)).place(x=70,y=100)
Entry(window,textvariable=url1,width=30).place(x=210,y=100)
Label(window,text='SELECT PX : ',background='#728C00',foreground='white',font=('verdana',13,BOLD)).place(x=70,y=130)
pixel = Combobox(window,width=10,textvariable=n,background="pink")
pixel['values'] = (
                    'mp4', 'webm', 'flv' , '3gp'
)
pixel.place(x=210,y=130)
pixel.current(0)
Label(window,text='PLEASE WAIT UNTIL THERE IS A MESSAGE OF DOWNLOAD COMPLETE : ',background='#FFA500',foreground='blue',font=('verdana',8,BOLD)).place(x=10,y=250)
Label(window,text='CREATED BY : ABHAY KUMAR ',background='#806517',foreground='white',font=('verdana',8,BOLD)).place(x=280,y=280)
window.resizable(0,0)
window.mainloop()
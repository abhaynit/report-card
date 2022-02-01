from tkinter import * 
from tkinter.ttk import * 


class GFG:
    def __init__(self,master=None):
        self.master = master 
        self.x =1
        self.y=0
        self.canvas = Canvas(master,width=500,height=500,bg="yellow")

        self.rectangle = self.canvas.create_rectangle(5,5,25,25,fill="black")
        self.rectangle1 = self.canvas.create_rectangle(50,50,78,78,fill="black")

        self.canvas.pack()
        self.movement()

    def movement(self):
        self.canvas.move(self.rectangle,self.x,self.y)
        self.canvas.after(5,self.movement)
        
    def left(self,event):
        print(event.keysym)
        self.x=-5 
        self.y=0 

    def right(self,event):
        print(event.keysym)
        self.x=5 
        self.y=0 

    def up(self,event):
        print(event.keysym)
        self.x=0 
        self.y=-5 

    def down(self,event):
        print(event.keysym)
        self.x=-0 
        self.y=5



master = Tk()
gfg = GFG(master)

master.bind("<KeyPress-Left>",lambda e: gfg.left(e))
master.bind("<KeyPress-Right>",lambda g: gfg.right(g))
master.bind("<KeyPress-Up>",lambda e: gfg.up(e))
master.bind("<KeyPress-Down>",lambda e: gfg.down(e))

mainloop()
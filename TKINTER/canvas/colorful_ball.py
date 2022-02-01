from tkinter import * 

root =Tk()

c = Canvas(root,heigh=500,width=250)

#line = c.create_line(0,100,40,100,fill="green")

#line1 = c.create_line(0,120,200,120,fill="green")

#line2 = c.create_line(108,120,108,40,fill="green")



arc1 = c.create_arc(40,150,200,310,start =0,extent=45,fill="red")
arc11 = c.create_arc(40,150,200,310,start =45,extent=45,fill="pink")


arc2 = c.create_arc(40,150,200,310,start =90,extent=45,fill="blue")
arc22 = c.create_arc(40,150,200,310,start =135,extent=45,fill="cyan")


arc3 = c.create_arc(40,150,200,310,start =180,extent=45,fill="brown")
ar33 = c.create_arc(40,150,200,310,start =225,extent=45,fill="gold")


arc4 = c.create_arc(40,150,200,310,start =270,extent=45,fill="green")
arc44 = c.create_arc(40,150,200,310,start =315,extent=45,fill="silver")


#oval = c.create_oval(80,30,140,150,fill="blue")

c.pack()
root.mainloop()
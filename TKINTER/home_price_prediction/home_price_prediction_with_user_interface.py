from tkinter import *
root = Tk()
root.configure(bg='pink')


root.minsize(500,500)
ab1 = Label(root,text="ENTER THE AREA : ")
ab1.place(x=100,y=100)
ab = Entry(root)
ab.place(x=350,y=100)

ab1 = Label(root,text="ENTER THE NO OF BEDROOM : ")
ab1.place(x=100,y=150)
ac = Entry(root)
ac.place(x=350,y=150)

ab1 = Label(root,text="ENTER THE NO OF YEAR OLD : ")
ab1.place(x=100,y=200)
ad = Entry(root)
ad.place(x=350,y=200)

result = Label(root)
result.place(x=300,y=300)
def pri():
    import pickle
    with open("home_price_new","rb") as f:
        mod = pickle.load(f)
    a = ab.get()
    b = ac.get()
    c = ad.get()
    ty = (mod.predict([[int(a),int(b),int(c)]]))
    result.configure(text = "THE PRICE OF HOME IS : " + str(ty))


button = Button(root,text = "find",command=pri)
button.place(x=200,y= 250)
button = Button(root,text = "find",command=pri)
button.place(x=200,y= 250)
root.mainloop()
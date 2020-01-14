from tkinter import *
master = Tk() 
master.title("Welcome to Standalone app")
master.geometry('350x200')
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

def clicked():
    res = "Welcome to " + e1.get() + e2.get()
    lbl.configure(text= res)
btn = Button(master, text="Click Me", command=clicked)
btn.grid(column=1, row=2)

lbl = Label(master, text="Hello")
lbl.grid(column=0, row=3)

mainloop() 

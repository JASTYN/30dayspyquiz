import tkinter
from tkinter import*

win= Tk()

c = Canvas(win, height=250, width=300,bg='blue')
c.pack()
           

l = Label(c, text='Username')
l.pack(side=LEFT)
e = Entry(c)
e.pack(side=RIGHT)
        
           
win.mainloop()
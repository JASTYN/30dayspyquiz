import tkinter
from tkinter import*

win=Tk()


l = Label(win, text='Username')
l.pack(side=LEFT)
e = Entry(win)
e.pack(side=RIGHT)

t = Text(win)
t.insert(INSERT, 'HELLO')
t.pack()


win.mainloop()
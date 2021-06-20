import tkinter
from tkinter import*

win=Tk()

c1= IntVar()
c2=IntVar()
cb= Checkbutton(win, text='music', offvalue=0, onvalue=1, height=5, width=10, variable=c1)

cb.pack()
cb1= Checkbutton(win, text='value', offvalue=0, onvalue=1, height=5, width=10, variable=c2)
cb1.pack()

var = IntVar()
r1= Radiobutton(win, text='option1', variable=var, value=1)
r1.pack()

win.mainloop()
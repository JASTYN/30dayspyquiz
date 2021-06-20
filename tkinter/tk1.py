import tkinter
from tkinter import*

win=Tk()
win.geometry("800x600")

b = Button(win, text='button')
#b.pack()
b.grid(row=1, column=1)
b2 = Button(win, text='buttoni', command=print('hi'),padx=20, pady=50,activeforeground='blue')
#b2.pack()
b2.place(x=100, y=200)

win.mainloop()
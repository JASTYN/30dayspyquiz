
from tkinter import *
window = Tk()
window.title('Label example')

var1 = IntVar()
Checkbutton(window, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(window, text='female', variable=var2).grid(row=1, sticky=W)

Label(window, text='First Name').grid(row=2)
Label(window, text='Last Name').grid(row=3)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)


window.mainloop()
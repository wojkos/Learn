from tkinter import *

window = Tk()

def km_to_miles():
	print('Success')

e1_val = StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=0)

b1=Button(window,text='Execute',command=km_to_miles)
b1.grid(row=0,column=1)

t1=Text(window,height = 1,width = 20)
t1.grid(row = 0, column = 2)

window.mainloop()
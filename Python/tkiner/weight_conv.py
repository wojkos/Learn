from tkinter import *

window = Tk()

def kg_to():
	grams = float(e1_val.get())*1000
	pounds = float(e1_val.get())*2.20462
	ounces = float(e1_val.get())*35,274
	t1.insert(END,grams)
	t2.insert(END,pounds)
	t3.insert(END,ounces)

e1_val = StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)
e2=Label(window,text="Kg")
e2.grid(row=0,column=0)

b1=Button(window,text='Zamień',command=kg_to)
b1.grid(row=0,column=2)

t1=Text(window,height = 1,width = 20)
t1.grid(row = 1, column = 1)
t1_lab=Label(window,text="gramy")
t1_lab.grid(row = 1, column = 0)

t2=Text(window,height = 1,width = 20)
t2.grid(row = 2, column = 1)
t2_lab=Label(window,text="funty")
t2_lab.grid(row = 2, column = 0)
t3=Text(window,height = 1,width = 20)
t3.grid(row = 3, column = 1)
t3_lab=Label(window,text="uncje")
t3_lab.grid(row = 3, column = 0)

window.mainloop()
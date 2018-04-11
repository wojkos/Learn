"""
a program that stores this book information:

user can:
view all records
search an entry
add entry
update entry
delete
close
"""
from tkinter import *
import base
window = Tk()
# labels
l1=Label(window,text="Title")
l1.grid(row = 0, column = 0)
l1=Label(window,text="Author")
l1.grid(row = 0, column = 2)
l1=Label(window,text="Year")
l1.grid(row = 1, column = 0)
l1=Label(window,text="ISBN")
l1.grid(row = 1, column = 2)
# inserts
title_text = StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
author_text = StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)
year_text = StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)
ISBN_text = StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# buttons
b1=Button(window,text='View all',width=12)
b1.grid(row=2,column=3)
b2=Button(window,text='Search entry',width=12)
b2.grid(row=3,column=3)
b3=Button(window,text='Add entry',width=12)
b3.grid(row=4,column=3)
b4=Button(window,text='Update',width=12)
b4.grid(row=5,column=3)
b5=Button(window,text='Delete',width=12)
b5.grid(row=6,column=3)
b6=Button(window,text='Close',width=12)
b6.grid(row=7,column=3)

window.mainloop()
# def kg_to():
# 	grams = float(e1_val.get())*1000
# 	pounds = float(e1_val.get())*2.20462
# 	ounces = float(e1_val.get())*35,274
# 	t1.insert(END,grams)
# 	t2.insert(END,pounds)
# 	t3.insert(END,ounces)

# e1_val = StringVar()
# e1=Entry(window,textvariable=e1_val)
# e1.grid(row=0,column=1)
# e2=Label(window,text="Kg")
# e2.grid(row=0,column=0)

# b1=Button(window,text='Zamień',command=kg_to)
# b1.grid(row=0,column=2)

# t1=Text(window,height = 1,width = 20)
# t1.grid(row = 1, column = 1)
# t1_lab=Label(window,text="gramy")
# t1_lab.grid(row = 1, column = 0)

# t2=Text(window,height = 1,width = 20)
# t2.grid(row = 2, column = 1)
# t2_lab=Label(window,text="funty")
# t2_lab.grid(row = 2, column = 0)
# t3=Text(window,height = 1,width = 20)
# t3.grid(row = 3, column = 1)
# t3_lab=Label(window,text="uncje")
# t3_lab.grid(row = 3, column = 0)

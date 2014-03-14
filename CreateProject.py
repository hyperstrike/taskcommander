#!/usr/bin/python
from Tkinter import *
import tkSimpleDialog
import ttk

### Inspired by code from: 
### http://www.java2s.com/Code/Python/GUI-Tk/AddacheckboxtoaDialog.htm

class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):
        Label(master, text="Project Name: ").grid(row=0, column=0, sticky=W, pady=3)
        Label(master, text="Project Description: ").grid(row=1, column=0, sticky=W, pady=3)
	Label(master, text="Project Owner ID: ").grid(row=2, column=0, sticky=W, pady=3)
	Label(master, text="Project Due Date: ").grid(row=2, column=2, sticky=W, padx=15, pady=3)
    
        self.e1 = Entry(master)
        self.e2 = Entry(master)
	self.e3 = Entry(master)
	self.e4 = Entry(master)
    
        self.e1.grid(row=0, column=1, sticky=W, pady=3)
        self.e2.grid(row=1, column=1, sticky=W, pady=3)
	self.e3.grid(row=2, column=1, sticky=W, pady=3)
	self.e4.grid(row=2, column=3, sticky=W, pady=3)
    
        Label(master, text="Associated Tasks: ").grid(row=4, column=0, sticky=W, pady=10)
	
	Label(master, text="Task Name: ").grid(row=5, column=0, sticky=W)
	Label(master, text="Task Owner ID: ").grid(row=5, column=2, padx=15, sticky=W)
	Label(master, text="Task Due Date: ").grid(row=6, column=0, sticky=W, pady=3)
	
	self.e5 = Entry(master)
	self.e6 = Entry(master)
	self.e7 = Entry(master)

	self.e5.grid(row=5, column=1, sticky=W, pady=3)
	self.e6.grid(row=5, column=3, sticky=W, pady=3)
	self.e7.grid(row=6, column=1, sticky=W, pady=3)
	
	b1 = Button(master, text="Add Task")
	#checkbutton.grid(columnspan=2, sticky=W, pady=3)
	b1.grid(row=6, column=2, sticky=W, padx=15, pady=3)

    
    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
	third = self.e3.get()
	fourth = self.e4.get()
        print first, second, third, fourth

root = Tk()
root.title("Create Project")
d = MyDialog(root)
print d.result


#root.mainloop()

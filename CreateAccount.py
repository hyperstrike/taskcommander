#!/usr/bin/python
from Tkinter import *
import tkSimpleDialog
import ttk

### Inspired by code from: 
### http://www.java2s.com/Code/Python/GUI-Tk/AddacheckboxtoaDialog.htm

class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):
        Label(master, text="First Name:").grid(row=0, column=0)
        Label(master, text="Last Name:").grid(row=0, column=2)
	Label(master, text="ID Number:").grid(row=1, column=0)
	Label(master, text="D.O.B.").grid(row=1, column=2)
    
        self.e1 = Entry(master)
        self.e2 = Entry(master)
	self.e3 = Entry(master)
	self.e4 = Entry(master)
    
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=0, column=3)
	self.e3.grid(row=1, column=1)
	self.e4.grid(row=1, column=3)
    
	self.cb1 = Checkbutton(master, text="Global Admin")
	self.cb2 = Checkbutton(master, text="Project Manager")
	self.cb3 = Checkbutton(master, text="Task Receiver")
	self.cb1.grid(row=4, columnspan=2, sticky=W)        
	self.cb2.grid(row=4, column=2, sticky=W)     
	self.cb3.grid(row=5, columnspan=2, sticky=W)     
	#self.cb1.grid(row=2, columnspan=2, sticky=W)
    
    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
	third = self.e3.get()
	fourth = self.e4.get()
        print first, second, third, fourth

root = Tk()
root.title("Create Account")
d = MyDialog(root)
print d.result


#root.mainloop()

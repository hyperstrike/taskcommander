#!/usr/bin/python
from Tkinter import *
import tkSimpleDialog
import ttk

### Inspired by code from: 
### http://www.java2s.com/Code/Python/GUI-Tk/AddacheckboxtoaDialog.htm

class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):
        Label(master, text="Employee ID: ").grid(row=0, column=0, padx=3, pady=3, sticky=W)
        Label(master, text="Password: ").grid(row=1, column=0, padx=3, pady=3, sticky=W)
    
        self.e1 = Entry(master)
        self.e2 = Entry(master, show="*", width=20)
    
        self.e1.grid(row=0, column=1, padx=3, pady=3, sticky=W)
        self.e2.grid(row=1, column=1, padx=3, pady=3, sticky=W)
    
    
    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        #print first, second

root = Tk()
root.title("Login")
d = MyDialog(root)
print d.result


#root.mainloop()

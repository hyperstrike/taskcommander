#!/usr/bin/python3
import sys
import string
import tkinter as tk
from tkinter import *
from tkinter import ttk

# This program was built upon Bryan Oakley's Toplevel example
# on stackoverflow.com

# It has been modified to test generation and data collection of windows
# generated from clicking on options from the main window

# TODO:
# - additional field formatting for dates and ID numbers
# - determining how to obtain which access level the user chose
# - refine look of GUI
# - integration

class MainWindow(tk.Frame):
    counter = 0
    #login variables
    login_userName = "invalid"
    login_password = "invalid"
    #account variables
    account_firstName = "invalid"
    account_lastName = "invalid"
    account_employeeID = "invalid"
    account_DOB = "invalid"
    acount_type = "invalid"
    #task variables
    task_name = "invalid"
    task_description = "invalid"
    task_ownerID = "invalid"
    task_dueDate = "invalid"



    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        #info bar
        tk.Label(self, text="Window to Test").grid(row=0, column=0, pady=5)
        tk.Label(self, text="=============").grid(row=1, column=0)
        tk.Label(self, text="Return Value #1").grid(row=0, column=2)
        tk.Label(self, text="=============").grid(row=1, column=2)
        tk.Label(self, text="Return Value #2").grid(row=0, column=4)
        tk.Label(self, text="=============").grid(row=1, column=4)
        tk.Label(self, text="Return Value #3").grid(row=0, column=6)
        tk.Label(self, text="=============").grid(row=1, column=6)
        tk.Label(self, text="Return Value #4").grid(row=0, column=8)
        tk.Label(self, text="=============").grid(row=1, column=8)
        
        #login field
        self.button = tk.Button(self, text="Log In", command=self.create_login_window)
        self.button.grid(row=2, column=0, pady=5)
        tk.Label(self, text="User:").grid(row=2, column=1)
        self.ret1 = tk.Label(self, text='invalid')
        self.ret1.grid(row=2, column=2)
        tk.Label(self, text="Pass:").grid(row=2, column=3)
        self.ret2 = tk.Label(self, text='invalid')
        self.ret2.grid(row=2, column=4)
        
        #create account field
        self.button = tk.Button(self, text="Create Account", command=self.create_account_window)
        self.button.grid(row=3, column=0, pady=5)
        tk.Label(self, text="First Name:").grid(row=3, column=1)
        self.ret3 = tk.Label(self, text='invalid')
        self.ret3.grid(row=3, column=2)
        tk.Label(self, text="Last Name:").grid(row=3, column=3)
        self.ret4 = tk.Label(self, text='invalid')
        self.ret4.grid(row=3, column=4)
        tk.Label(self, text="ID Number:").grid(row=3, column=5)
        self.ret5 = tk.Label(self, text='invalid')
        self.ret5.grid(row=3, column=6)
        tk.Label(self, text="Date of Birth:").grid(row=3, column=7)
        self.ret6 = tk.Label(self, text='invalid')
        self.ret6.grid(row=3, column=8)
        
        #create task field
        self.button = tk.Button(self, text="Create Task", command=self.create_task_window)
        self.button.grid(row=4, column=0, pady=5)
        tk.Label(self, text="Task Name:").grid(row=4, column=1)
        self.taskRet1 = tk.Label(self, text='invalid')
        self.taskRet1.grid(row=4, column=2)
        tk.Label(self, text="Task Description:").grid(row=4, column=3)
        self.taskRet2 = tk.Label(self, text='invalid')
        self.taskRet2.grid(row=4, column=4)
        tk.Label(self, text="Task Owner ID:").grid(row=4, column=5)
        self.taskRet3 = tk.Label(self, text='invalid')
        self.taskRet3.grid(row=4, column=6)
        tk.Label(self, text="Task Due Date:").grid(row=4, column=7)
        self.taskRet4 = tk.Label(self, text='invalid')
        self.taskRet4.grid(row=4, column=8)
        
        tk.Label(self, text="*").grid(row=5, column=0, pady=5)
        tk.Label(self, text="TaskCommander Window Testing Module *ALPHA*").grid(row=6, column=0)
    
    def create_login_window(self):
        self.counter += 1
        logWin = tk.Toplevel(self)
        logWin.wm_title("Log In")
        tk.Label(logWin, text="Employee ID:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        tk.Label(logWin, text="Password:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        
        logWin.e1 = Entry(logWin)
        logWin.e2 = Entry(logWin, show="*", width=20)
        
        logWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        logWin.e2.grid(row=1, column=1, padx=6, pady=6, sticky=W)
        
        def commit_login():
            self.ret1['text'] = logWin.e1.get()
            self.ret2['text'] = logWin.e2.get()
        
        logWin.acceptButton = tk.Button(logWin, text="Accept", command=commit_login)
        logWin.cancelButton = tk.Button(logWin, text="Cancel", command=logWin.destroy)
        logWin.acceptButton.grid(row=2, column=1, padx=6, pady=6, sticky=W)
        logWin.cancelButton.grid(row=2, column=1, padx=6, pady=6, sticky=E)

    def create_account_window(self):
        self.counter += 1
        accWin = tk.Toplevel(self)
        accWin.wm_title("Create Account")
        tk.Label(accWin, text="First Name:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        tk.Label(accWin, text="Last Name:").grid(row=0, column=2, padx=6, pady=6, sticky=W)
        tk.Label(accWin, text="Employee ID:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        tk.Label(accWin, text="D.O.B. (MM/DD/YYYY)").grid(row=1, column=2, padx=6, pady=6, sticky=W)
        
        accWin.e1 = Entry(accWin)
        accWin.e2 = Entry(accWin)
        accWin.e3 = Entry(accWin)
        accWin.e4 = Entry(accWin)
        
        accWin.e1.grid(row=0, column=1, padx=3, pady=3, sticky=W)
        accWin.e2.grid(row=0, column=3, padx=3, pady=3, sticky=W)
        accWin.e3.grid(row=1, column=1, padx=3, pady=3, sticky=W)
        accWin.e4.grid(row=1, column=3, padx=3, pady=3, sticky=W)
        
        #select access level
        tk.Label(accWin, text="Select account type:").grid(row=3, column=0, padx=6, pady=6)
        var = IntVar()
        accWin.r1 = tk.Radiobutton(accWin, text="Global Admin", variable=var, value=1, command=None)
        accWin.r2 = tk.Radiobutton(accWin, text="Project Manager", variable=var, value=2, command=None)
        accWin.r3 = tk.Radiobutton(accWin, text="Task Receiver", variable=var, value=3, command=None)
        accWin.r1.grid(row=4, column=0)
        accWin.r2.grid(row=4, column=1)
        accWin.r3.grid(row=4, column=2)
        
        def commit_account():
            self.ret3['text'] = accWin.e1.get()
            self.ret4['text'] = accWin.e2.get()
            self.ret5['text'] = accWin.e3.get()
            self.ret6['text'] = accWin.e4.get()
            #account type?
            
        accWin.acceptButton = tk.Button(accWin, text="Accept", command=commit_account)
        accWin.cancelButton = tk.Button(accWin, text="Cancel", command=accWin.destroy)
        accWin.acceptButton.grid(row=6, column=1, padx=6, pady=6, sticky=W)
        accWin.cancelButton.grid(row=6, column=1, padx=6, pady=6, sticky=E)
        
    def create_task_window(self):
        self.counter += 1
        tskWin = tk.Toplevel(self)
        tskWin.wm_title("Create Task")
        tk.Label(tskWin, text="Task Name:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        tk.Label(tskWin, text="Task Description:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        tk.Label(tskWin, text="Task Owner ID:").grid(row=2, column=0, padx=6, pady=6, sticky=W)
        tk.Label(tskWin, text="Task Due Date (MM/DD/YYYY):").grid(row=2, column=2, padx=6, pady=6, sticky=W)
        
        tskWin.e1 = Entry(tskWin)
        tskWin.e2 = Entry(tskWin)
        tskWin.e3 = Entry(tskWin)
        tskWin.e4 = Entry(tskWin)
        
        tskWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        tskWin.e2.grid(row=1, column=1, padx=6, pady=6, sticky=W)
        tskWin.e3.grid(row=2, column=1, padx=6, pady=6, sticky=W)
        tskWin.e4.grid(row=2, column=3, padx=6, pady=6, sticky=W)
        
        def commit_task():
            self.taskRet1['text'] = tskWin.e1.get()
            self.taskRet2['text'] = tskWin.e2.get()
            self.taskRet3['text'] = tskWin.e3.get()
            self.taskRet4['text'] = tskWin.e4.get()
            
        tskWin.acceptButton = tk.Button(tskWin, text="Accept", command=commit_task)
        tskWin.cancelButton = tk.Button(tskWin, text="Cancel", command=tskWin.destroy)
        tskWin.acceptButton.grid(row=3, column=1, padx=6, pady=6, sticky=W)
        tskWin.cancelButton.grid(row=3, column=1, padx=6, pady=6, sticky=E)
    
        
if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="left", fill="both", expand=True)
    root.mainloop()

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
    account_type = "invalid"
    #task variables
    task_name = "invalid"
    task_description = "invalid"
    task_ownerID = "invalid"
    task_dueDate = "invalid"

    #login getters
    def getUserName(self):
    	return login_userName

    def getPassword(self):
    	return login_password

    #account getters
    def getFirstName(self):
    	return account_firstName

    def getLastName(self):
    	return account_lastName

    def getEmployeeID(self):
    	return account_employeeID

    def getDOB(self):
    	return account_DOB

    def getAccountType(self):
    	return account_type

    #task getters
    def getTaskName(self):
    	return task_name

    def getTaskDescription(self):
    	return task_description

    def getOwnerID(self):
    	return task_ownerID

    def getTaskDueDate(self):
    	return task_dueDate



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
        self.login_userName = tk.Label(self, text='invalid')
        self.login_userName.grid(row=2, column=2)
        tk.Label(self, text="Pass:").grid(row=2, column=3)
        self.login_password = tk.Label(self, text='invalid')
        self.login_password.grid(row=2, column=4)
        
        #create account field
        self.button = tk.Button(self, text="Create Account", command=self.create_account_window)
        self.button.grid(row=3, column=0, pady=5)
        tk.Label(self, text="First Name:").grid(row=3, column=1)
        self.account_firstName = tk.Label(self, text='invalid')
        self.account_firstName.grid(row=3, column=2)
        tk.Label(self, text="Last Name:").grid(row=3, column=3)
        self.account_lastName = tk.Label(self, text='invalid')
        self.account_lastName.grid(row=3, column=4)
        tk.Label(self, text="ID Number:").grid(row=3, column=5)
        self.account_employeeID = tk.Label(self, text='invalid')
        self.account_employeeID.grid(row=3, column=6)
        tk.Label(self, text="Date of Birth:").grid(row=3, column=7)
        self.account_DOB = tk.Label(self, text='invalid')
        self.account_DOB.grid(row=3, column=8)
        #add in TYPE field
        
        #create task field
        self.button = tk.Button(self, text="Create Task", command=self.create_task_window)
        self.button.grid(row=4, column=0, pady=5)
        tk.Label(self, text="Task Name:").grid(row=4, column=1)
        self.task_name = tk.Label(self, text='invalid')
        self.task_name.grid(row=4, column=2)
        tk.Label(self, text="Task Description:").grid(row=4, column=3)
        self.task_description = tk.Label(self, text='invalid')
        self.task_description.grid(row=4, column=4)
        tk.Label(self, text="Task Owner ID:").grid(row=4, column=5)
        self.task_ownerID = tk.Label(self, text='invalid')
        self.task_ownerID.grid(row=4, column=6)
        tk.Label(self, text="Task Due Date:").grid(row=4, column=7)
        self.task_dueDate = tk.Label(self, text='invalid')
        self.task_dueDate.grid(row=4, column=8)

        #create project field
        self.button = tk.Button(self, text="Create Project", command=self.create_project_window)
        self.button.grid(row=5, column=0)
        
        tk.Label(self, text="*").grid(row=6, column=0, pady=5)
        tk.Label(self, text="TaskCommander Window Testing Module *BETA*").grid(row=7, column=0)

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
        
        accWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        accWin.e2.grid(row=0, column=3, padx=6, pady=6, sticky=W)
        accWin.e3.grid(row=1, column=1, padx=6, pady=6, sticky=W)
        accWin.e4.grid(row=1, column=3, padx=6, pady=6, sticky=W)

    def create_project_window(self):
        self.counter += 1
        projWin = tk.Toplevel(self)
        projWin.wm_title("Create Project")
        tk.Label(projWin, text="Project Name:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Description:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Owner ID:").grid(row=2, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Associated Tasks:").grid(row=3, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Task Name:").grid(row=4, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Task Due Date:").grid(row=4, column=2, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Add Project Viewers:").grid(row=6, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Viewer ID:").grid(row=7, column=0, padx=6, pady=6, sticky=W)
        
        projWin.e1 = Entry(projWin)
        projWin.e2 = Entry(projWin)
        projWin.e3 = Entry(projWin)
        projWin.e4 = Entry(projWin)
        projWin.e5 = Entry(projWin)
        projWin.e6 = Entry(projWin)

        projWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        projWin.e2.grid(row=1, column=1, padx=6, pady=6, sticky=W)
        projWin.e3.grid(row=2, column=1, padx=6, pady=6, sticky=W)
        projWin.e4.grid(row=4, column=1, padx=6, pady=6, sticky=W)
        projWin.e5.grid(row=4, column=3, padx=6, pady=6, sticky=W)
        projWin.taskButton = tk.Button(logWin, text="Add Task", command=commit_task)
        projWin.taskButton.grid(row=5, column=1, padx=6, pady=6, sticky=W)
        projWin.e6.grid(row=7, column=1, padx=6, pady=6, sticky=W)

        def commit_task():
            print("task commit")
            #add task to dictionary

        def commit_viewer():
            print("viewer commit")
            #add viewer to dictionary

        projWin.viewerButton = tk.Button(logWin, text="Add Viewer", command=commit_viewer)
        projWin.viewerButton.grid(row=7, column=2, padx=6, pady=6, sticky=W)

        projWin.acceptButton = tk.Button(logWin, text="Accept", command=commit_project)
        projWin.cancelButton = tk.Button(logWin, text="Cancel", command=projWin.destroy)
        projWin.acceptButton.grid(row=8, column=0, padx=6, pady=6, sticky=W)
        projWin.cancelButton.grid(row=8, column=1, padx=6, pady=6, sticky=W)

    
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
            self.login_userName['text'] = logWin.e1.get()
            self.login_password['text'] = logWin.e2.get()
            logWin.destroy()
        
        logWin.newAccountButton = tk.Button(logWin, text="New Account", command=self.create_account_window)
        logWin.acceptButton = tk.Button(logWin, text="Accept", command=commit_login)
        logWin.cancelButton = tk.Button(logWin, text="Cancel", command=logWin.destroy)
        logWin.newAccountButton.grid(row=2, column=0, padx=6, pady=6, sticky=W)
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
        
        accWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        accWin.e2.grid(row=0, column=3, padx=6, pady=6, sticky=W)
        accWin.e3.grid(row=1, column=1, padx=6, pady=6, sticky=W)
        accWin.e4.grid(row=1, column=3, padx=6, pady=6, sticky=W)

        #select access level
        def set_admin():
            is_admin = True

        tk.Label(accWin, text="Select account type:").grid(row=3, column=0, padx=6, pady=6)
        var = IntVar()
        accWin.r1 = tk.Radiobutton(accWin, text="Project Manager", variable=var, value=1, command=None)
        accWin.r2 = tk.Radiobutton(accWin, text="Task Receiver", variable=var, value=2, command=set_admin)
        accWin.r1.grid(row=4, column=0)
        accWin.r2.grid(row=4, column=1)
        
        
        def commit_account():
            self.account_firstName['text'] = accWin.e1.get()
            self.account_lastName['text'] = accWin.e2.get()
            self.account_employeeID['text'] = accWin.e3.get()
            self.account_DOB['text'] = accWin.e4.get()
            #account type?
            accWin.destroy()
            
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
            self.task_name['text'] = tskWin.e1.get()
            self.task_description['text'] = tskWin.e2.get()
            self.task_ownerID['text'] = tskWin.e3.get()
            self.task_dueDate['text'] = tskWin.e4.get()
            tskWin.destroy()
            
        tskWin.acceptButton = tk.Button(tskWin, text="Accept", command=commit_task)
        tskWin.cancelButton = tk.Button(tskWin, text="Cancel", command=tskWin.destroy)
        tskWin.acceptButton.grid(row=3, column=1, padx=6, pady=6, sticky=W)
        tskWin.cancelButton.grid(row=3, column=1, padx=6, pady=6, sticky=E)
    
        
if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="left", fill="both", expand=True)
    root.mainloop()

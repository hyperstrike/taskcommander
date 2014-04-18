#!/usr/bin/python3
import os,sys,string, calendar, time
import tkinter as tk
from tkinter import *
from tkinter import ttk


ALL=N+S+E+W
numButtons = 5
buttonBounds = [5,6,7,8,9]


class Application(Frame):
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
    #calendar variables *Thx Teresa!*
    strdays = "Mon Tue Wed Thu Fri Sat Sun"
    dictmonths = {'1':'Jan','2':'Feb','3':'Mar',
                  '4':'Apr','5':'May','6':'Jun',
                  '7':'Jul','8':'Aug','9':'Sep',
                  '10':'Oct','11':'Nov','12':'Dec'}
 
    year = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]
    strdate = (str(year) + "/" + dictmonths[str(month)] + "/" + str(day))

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


    def __init__(self,master=None):
        Frame.__init__(self,master)
        #self.wm_title('Task Commander Test GUI')
        self.grid(sticky=ALL)

        w = root.winfo_screenwidth()
        w = int(w/6)
        h = root.winfo_screenheight()
        h = int(h/6)
        root.geometry("900x400" + "+" + str(w) + "+" + str(h))

        ############################################
        ############ "CREATE" FRAME ############
        ############################################

        #logo~!
        self.rowconfigure(0)
        self.columnconfigure(0)
        self.logo = tk.PhotoImage(file='logo.gif')
        self.logo2 = tk.PhotoImage(file='logo2.gif')
        logoFrame=Frame(self,bg='grey',width=400)
        logoFrame.grid(row=0,column=0,rowspan=1,columnspan=3,sticky=ALL)
        myLogo = tk.Label(logoFrame, image=self.logo).grid(row=2,column=0,columnspan=2)
        #Label(logoFrame, text="*Insert LOGO Here*").grid(row=3, column=0)
        
        #buttons!
        myframe1=Frame(self,bg='white')
        myframe1.grid(row=1,column=0,rowspan=2,columnspan=2,sticky=ALL)
        login_button = Button(myframe1, text="Log In", command=self.create_login_window)
        login_button.grid(column=0, row=0)

        account_button = Button(myframe1, text="Create Account", command=self.create_account_window)
        account_button.grid(column=0, row=2)

        project_button = Button(myframe1, text="Create Project", command=self.create_project_window)
        project_button.grid(column=0, row=4)

        task_button = Button(myframe1, text="Create Task", command=self.create_task_window)
        task_button.grid(column=0, row=6)

        ############################################
        ############     TAB FRAME      ############
        ############################################
        global numButtons
        global buttonBounds
        tabFrame=Frame(self,bg='white', height=600, width=455)
        self.button1text = tk.StringVar()
        self.button2text = tk.StringVar()
        self.button3text = tk.StringVar()
        self.button4text = tk.StringVar()
        self.button5text = tk.StringVar()
        self.button1text.set("Project " + str(buttonBounds[0]))
        self.button2text.set("Project " + str(buttonBounds[1]))
        self.button3text.set("Project " + str(buttonBounds[2]))
        self.button4text.set("Project " + str(buttonBounds[3]))
        self.button5text.set("Project " + str(buttonBounds[4]))

        self.myLogo2 = tk.Label(tabFrame, image=self.logo2).grid(row=0, column=0, columnspan=3)  
            

        arrowLeft = Button(tabFrame,text="<", command=self.GoLeft).grid(column=0, row=1)
        arrowRight = Button(tabFrame,text=">", command=self.GoRight).grid(column=7, row=1)

        
        test = Button(tabFrame,text="Open", command=self.OnButtonClick1, width=200)
        myButtons = [test] * 50

        myButtons[0] = tk.Button(tabFrame,textvariable=(str(self.button1text)), command=self.OnButtonClick1, width=8).grid(column=1, row=1)
        myButtons[1] = tk.Button(tabFrame,textvariable=(str(self.button2text)), command=self.OnButtonClick2, width=8).grid(column=2, row=1)
        myButtons[2] = tk.Button(tabFrame,textvariable=(str(self.button3text)), command=self.OnButtonClick3, width=8).grid(column=3, row=1)
        myButtons[3] = tk.Button(tabFrame,textvariable=(str(self.button4text)), command=self.OnButtonClick4, width=8).grid(column=4, row=1)
        myButtons[4] = tk.Button(tabFrame,textvariable=(str(self.button5text)), command=self.OnButtonClick5, width=8).grid(column=5, row=1)

        tabFrame.grid(row=0,column=2,rowspan=1,columnspan=1,sticky=ALL)

        ############################################
        ############ PROJECT FRAME ############
        ############################################
        self.rowconfigure(1)
        self.columnconfigure(1)
        myframe2=Frame(self,bg='grey', height = 600, width = 455)
        myframe2.grid(row=1,column=2,rowspan=1,columnspan=1,sticky=ALL)

        ############################################
        ############ INFO FRAME ############
        ############################################
        self.rowconfigure(0)
        self.columnconfigure(2)
        #title frame
        titleFrame=Frame(self,bg='grey',width=400)
        titleFrame.grid(row=0,column=3,rowspan=1,columnspan=3,sticky=ALL)
        #progress bar!
        self.progress_bar = ttk.Progressbar(titleFrame, maximum=100)
        self.progress_bar.grid(row=5, column=1)
        self.progress_bar.step(25)
        self.update()

        ###### Complete Progress Bar example ######
        '''
           def __init__(self, master):
              tk.Frame.__init__(self, master)
              self.progress = ttk.Progressbar(self, maximum=10)
              self.progress.pack(expand=1, fill=tk.BOTH)
              self.progress.bind("<Button-1>", self._loop_progress)

           def _loop_progress(self, *args):
              for i in range(10):
                 self.progress.step(1)
                 # Necessary to update the progress bar appearance
                 self.update()
                 # Busy-wait
                 time.sleep(2)
         '''

        Label(titleFrame, text="*Insert Progress Bar Here*").grid(row=4, column=1)
        #info attributes
        myframe3=Frame(self,bg='white',width=400)
        myframe3.grid(row=1,column=3,rowspan=2,columnspan=3,sticky=ALL)
        Label(myframe3, text="Owner:").grid(row=3, column=1)
        Label(myframe3, text="Creator:").grid(row=4, column=1)
        Label(myframe3, text="Date of Creation:").grid(row=5, column=1)
        Label(myframe3, text="Due Date:").grid(row=6, column=1)
        Label(myframe3, text="Parent Project:").grid(row=7, column=1)
        self.info_ownerName = Label(myframe3, text="info_ownerName")
        self.info_ownerName.grid(row=3, column=2)
        self.info_creatorName = Label(myframe3, text="info_creatorName")
        self.info_creatorName.grid(row=4, column=2)
        self.info_dateOfCreation = Label(myframe3, text="info_dateOfCreation")
        self.info_dateOfCreation.grid(row=5, column=2)
        self.info_dueDate = Label(myframe3, text="info_dueDate")
        self.info_dueDate.grid(row=6, column=2)
        self.info_parentProject = Label(myframe3, text="info_parentProject")
        self.info_parentProject.grid(row=7, column=2)
        self.projText = tk.StringVar()
        self.projText.set("Project Stuff goes here. \n wordd.")
        myLabels = Label(titleFrame, textvariable=self.projText).grid(column=1, row=2)


    def OnButtonClick1(self):
        self.projText.set("Currently viewing Project " + str(buttonBounds[0]) + ".")

    def OnButtonClick2(self):
        self.projText.set("Currently viewing Project " + str(buttonBounds[1]) + ".")

    def OnButtonClick3(self):
        self.projText.set("Currently viewing Project " + str(buttonBounds[2]) + ".")
        
    def OnButtonClick4(self):
        self.projText.set("Currently viewing Project " + str(buttonBounds[3]) + ".")
        
    def OnButtonClick5(self):
        self.projText.set("Currently viewing Project " + str(buttonBounds[4]) + ".")

    def GoRight(self):
        global buttonBounds
        global numButtons
        for x in range (0, numButtons):
            buttonBounds[x] = buttonBounds[x] + 1
        self.button1text.set("Project " + str(buttonBounds[0]))
        self.button2text.set("Project " + str(buttonBounds[1]))
        self.button3text.set("Project " + str(buttonBounds[2]))
        self.button4text.set("Project " + str(buttonBounds[3]))
        self.button5text.set("Project " + str(buttonBounds[4]))  

    def GoLeft(self):
        global buttonBounds
        global numButtons
        for x in range (0, numButtons):
            buttonBounds[x] = buttonBounds[x] - 1
        self.button1text.set("Project " + str(buttonBounds[0]))
        self.button2text.set("Project " + str(buttonBounds[1]))
        self.button3text.set("Project " + str(buttonBounds[2]))
        self.button4text.set("Project " + str(buttonBounds[3]))
        self.button5text.set("Project " + str(buttonBounds[4])) 
        
    def create_account_window(self):
        self.counter += 1
        self.fName = StringVar()
        self.lName = StringVar()
        self.idNum = StringVar()
        self.dob = StringVar()
        accWin = Toplevel(self)
        root.withdraw() #hide parent window
        accWin.geometry('635x195+360+260')
        #t.wm_title("Window #%s" % self.counter)
        accWin.wm_title("Create Account")
        date_var2 = StringVar(accWin)
        date_var2.set(self.strdate)
        Label(accWin, text="First Name:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        Label(accWin, text="Last Name:").grid(row=0, column=2, padx=6, pady=6, sticky=W)
        Label(accWin, text="Employee ID:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        Label(accWin, text="D.O.B. (MM/DD/YYYY)").grid(row=1, column=2, padx=6, pady=6, sticky=W)

        accWin.e1 = Entry(accWin, textvariable=self.fName)
        accWin.e2 = Entry(accWin, textvariable=self.lName)
        accWin.e3 = Entry(accWin, textvariable=self.idNum)
        #accWin.e4 = Entry(accWin, textvariable=self.dob)
        accWin.e4 = Entry(accWin, textvariable=date_var2, bg="white", fg="blue", justify="center")

        date_button = tk.Button(accWin, text='Select Date', bg='#7fff00', relief=RAISED, command=lambda: self.fnCalendar(date_var2))
        date_button.grid(row=4, column=3)

        accWin.e1.grid(row=0, column=1, padx=3, pady=3, sticky=W)
        accWin.e1.focus_set()
        accWin.e2.grid(row=0, column=3, padx=3, pady=3, sticky=W)
        accWin.e3.grid(row=1, column=1, padx=3, pady=3, sticky=W)
        accWin.e4.grid(row=1, column=3, padx=3, pady=3, sticky=W)

        #date selection row 4

        #select priviledge level
        Label(accWin, text="Select account type:").grid(row=5, column=0, padx=6, pady=6)

        def set_admin(self):
            self.checkAdmin = True

        var = IntVar()
        accWin.r1 = Radiobutton(accWin, text="Global Admin", variable=var, command=set_admin(self))
        accWin.r2 = Radiobutton(accWin, text="User", variable=var, value=2, command=None)
        accWin.r1.grid(row=6, column=0)
        accWin.r2.grid(row=6, column=1)


        def commit_account():
            #bring main window back
            root.update()
            root.deiconify()

            print("commit account")
            accWin.destroy()

        accWin.acceptButton = Button(accWin, text="Accept", command=commit_account)
        accWin.cancelButton = Button(accWin, text="Cancel", command=accWin.destroy)
        accWin.acceptButton.grid(row=7, column=1, padx=6, pady=6, sticky=W)
        accWin.cancelButton.grid(row=7, column=1, padx=6, pady=6, sticky=E)

    ######### Lauren, do you want this changed? ############
    def create_login_window(self):
        self.counter += 1
        retUserName = StringVar()
        retPassword = StringVar()
        logWin = tk.Toplevel(self)
        logWin.geometry('335x120+400+260')
        logWin.wm_title("Log In")
        root.withdraw() #hide parent window
        tk.Label(logWin, text="Employee ID:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        tk.Label(logWin, text="Password:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        
        logWin.e1 = tk.Entry(logWin, textvariable=retUserName)
        logWin.e1.focus_set()
        logWin.e2 = tk.Entry(logWin, show="*", width=20, textvariable=retPassword)
        
        logWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        logWin.e2.grid(row=1, column=1, padx=6, pady=6, sticky=W)

        def commit_login():
            #bring main window back
            root.update()
            root.deiconify()

            #self.info_ownerName['text'] = logWin.e1.get()
            self.login_userName = logWin.e1.get()
            self.login_password = logWin.e2.get()
            print("login commit")
            #root.update() focus_set
            logWin.destroy()
    
        logWin.newAccountButton = tk.Button(logWin, text="New Account", command=self.create_account_window)
        logWin.acceptButton = tk.Button(logWin, text="Accept", command=commit_login)
        logWin.cancelButton = tk.Button(logWin, text="Cancel", command=logWin.destroy)
        logWin.newAccountButton.grid(row=2, column=0, padx=6, pady=6, sticky=W)
        logWin.acceptButton.grid(row=2, column=1, padx=6, pady=6, sticky=W)
        logWin.cancelButton.grid(row=2, column=1, padx=6, pady=6, sticky=E)

    #create task window
    def create_task_window(self):
        self.counter += 1
        tskWin = tk.Toplevel(self)
        tskWin.geometry('500x185+400+260')
        tskWin.wm_title("Create Task")
        root.withdraw() #hide parent window
        date_var2 = StringVar(tskWin)
        date_var2.set(self.strdate)
        
        tk.Label(tskWin, text="Task Name:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        tk.Label(tskWin, text="Task Description:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        tk.Label(tskWin, text="Task Owner ID:").grid(row=2, column=0, padx=6, pady=6, sticky=W)
        tk.Label(tskWin, text="Task Due Date (MM/DD/YYYY):").grid(row=3, column=0, padx=6, pady=6, sticky=W)
        
        tskWin.e1 = Entry(tskWin)
        tskWin.e2 = Entry(tskWin)
        tskWin.e3 = Entry(tskWin)
        tskWin.e4 = Entry(tskWin, textvariable=date_var2, bg="white", fg="blue", justify="center")
        
        tskWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        tskWin.e1.focus_set()
        tskWin.e2.grid(row=1, column=1, padx=6, pady=6, sticky=W)
        tskWin.e3.grid(row=2, column=1, padx=6, pady=6, sticky=W)
        tskWin.e4.grid(row=3, column=1, padx=6, pady=6, sticky=W)
        
        tskWin.btn = tk.Button(tskWin, text='Select Date', bg='#7fff00', relief=RAISED, command=lambda: self.fnCalendar(date_var2))
        tskWin.btn.grid(row=3, column=2, padx=6, pady=6, sticky=W)
        
        def commit_task():
            #bring main window back
            root.update()
            root.deiconify()

            self.task_name = tskWin.e1.get()
            self.task_description = tskWin.e2.get()
            self.task_ownerID = tskWin.e3.get()
            self.task_dueDate = tskWin.e4.get()
            print("task commit task")
            tskWin.destroy()

        tskWin.acceptButton = tk.Button(tskWin, text="Accept", command=commit_task)
        tskWin.cancelButton = tk.Button(tskWin, text="Cancel", command=tskWin.destroy)
        tskWin.acceptButton.grid(row=4, column=1, padx=6, pady=6, sticky=W)
        tskWin.cancelButton.grid(row=4, column=2, padx=6, pady=6, sticky=E)
        
    class tkCalendar:
      def __init__ (self, master, arg_year, arg_month, arg_day, arg_parent_updatable_var):
        self.update_var = arg_parent_updatable_var
        top = self.top = tk.Toplevel(master)
        top.title("Calendar")
        
        try:
            self.intmonth = int(arg_month)
        except:
            self.intmonth = int(1)
        
        self.canvas = tk.Canvas(top, width=200, height=155, relief=tk.RIDGE, background="white", borderwidth=1)
        stryear = str(arg_year)

        # year selected
        self.year_var = tk.StringVar()
        self.year_var.set(stryear)
        self.lblYear = tk.Label(top, textvariable = self.year_var, background="white")
        self.lblYear.place(x=85, y = 3)

        # month selected
        self.month_var = tk.StringVar()
        strnummonth = str(self.intmonth)
        strmonth = Application.dictmonths[strnummonth]
        self.month_var.set(strmonth)
 
        self.lblYear = tk.Label(top, textvariable = self.month_var, background="white")
        self.lblYear.place(x=85, y = 23)

        tagBaseButton = "Arrow"
        self.tagBaseNumber = "DayButton"
        
        #draw year arrows
        x,y = 40, 13 #43
        tagThisButton = "leftyear"
        tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
        self.fnCreateLeftArrow(self.canvas, x,y, tagFinalThisButton)
        x,y = 150, 13 #43
        tagThisButton = "rightyear"
        tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
        self.fnCreateRightArrow(self.canvas, x,y, tagFinalThisButton)
        
        #draw month arrows
        x,y = 40, 33 #63
        tagThisButton = "leftmonth"
        tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
        self.fnCreateLeftArrow(self.canvas, x,y, tagFinalThisButton)
        x,y = 150, 33 #63
        tagThisButton = "rightmonth"
        tagFinalThisButton = tuple((tagBaseButton,tagThisButton))
        self.fnCreateRightArrow(self.canvas, x,y, tagFinalThisButton)
        
        #Print days
        self.canvas.create_text(100,55, text=Application.strdays) #100,90
        self.canvas.pack (expand=1, fill=tk.BOTH)
        self.canvas.tag_bind("Arrow", "<ButtonRelease-1>", self.fnClick)
        self.canvas.tag_bind("Arrow", "<Enter>", self.fnOnMouseOver)
        self.canvas.tag_bind("Arrow", "<Leave>", self.fnOnMouseOut)
        self.fnFillCalendar()
 
      def fnCreateRightArrow(self, canv, x, y, strtagname):
        canv.create_polygon(x,y, [[x+0,y-5], [x+10, y-5] , [x+10,y-10] , [x+20,y+0], [x+10,y+10] , [x+10,y+5] , [x+0,y+5]],tags = strtagname , fill="blue", width=0)
 
      def fnCreateLeftArrow(self, canv, x, y, strtagname):
        canv.create_polygon(x,y, [[x+10,y-10], [x+10, y-5] , [x+20,y-5] , [x+20,y+5], [x+10,y+5] , [x+10,y+10] ],tags = strtagname , fill="blue", width=0)
 
      def fnClick(self,event):
        owntags = self.canvas.gettags(tk.CURRENT)
        if "rightyear" in owntags:
            intyear = int(self.year_var.get())
            intyear +=1
            stryear = str(intyear)
            self.year_var.set(stryear)
        if "leftyear" in owntags:
            intyear = int(self.year_var.get())
            intyear -=1
            stryear = str(intyear)
            self.year_var.set(stryear)
        if "rightmonth" in owntags:
            if self.intmonth < 12 :
                self.intmonth += 1
                strnummonth = str(self.intmonth)
                strmonth = Application.dictmonths[strnummonth]
                self.month_var.set(strmonth)
            else:
                self.intmonth = 1
                strnummonth = str(self.intmonth)
                strmonth = Application.dictmonths[strnummonth]
                self.month_var.set(strmonth)
                intyear = int(self.year_var.get())
                intyear +=1
                stryear = str(intyear)
                self.year_var.set(stryear)
        if "leftmonth" in owntags:
            if self.intmonth > 1:
                self.intmonth -= 1
                strnummonth = str(self.intmonth)
                strmonth = Application.dictmonths[strnummonth]
                self.month_var.set(strmonth)
            else:
                self.intmonth = 12
                strnummonth = str(self.intmonth)
                strmonth = MainWindow.dictmonths[strnummonth]
                self.month_var.set(strmonth)
                intyear = int(self.year_var.get())
                intyear -=1
                stryear = str(intyear)
                self.year_var.set(stryear)
        self.fnFillCalendar()
 
      def fnFillCalendar(self):
        init_x_pos = 20
        arr_y_pos = [70,90,110,130,150,170] #110,130,150,170,190,210
        intposarr = 0
        self.canvas.delete("DayButton")
        self.canvas.update()
        intyear = int(self.year_var.get())
        monthcal = calendar.monthcalendar(intyear, self.intmonth)
        for row in monthcal:
            xpos = init_x_pos
            ypos = arr_y_pos[intposarr]
            for item in row:
                stritem = str(item)
                if stritem == "0":
                    xpos += 27
                else:
                    tagNumber = tuple((self.tagBaseNumber,stritem))
                    self.canvas.create_text(xpos, ypos , text=stritem,tags=tagNumber)
                    xpos += 27
            intposarr += 1
        self.canvas.tag_bind("DayButton", "<ButtonRelease-1>", self.fnClickNumber)
        self.canvas.tag_bind("DayButton", "<Enter>", self.fnOnMouseOver)
        self.canvas.tag_bind("DayButton", "<Leave>", self.fnOnMouseOut)
 
      def fnClickNumber(self,event):
        owntags = self.canvas.gettags(tk.CURRENT)
        for x in owntags:
            if x not in ("current", "DayButton"):
                strdate = (str(self.year_var.get()) + "/" + str(self.month_var.get()) + "/" + str(x))
                self.update_var.set(strdate)
                self.top.withdraw()
 
      def fnOnMouseOver(self,event):
        self.canvas.move(tk.CURRENT, 1, 1)
        self.canvas.update()
 
      def fnOnMouseOut(self,event):
        self.canvas.move(tk.CURRENT, -1, -1)
        self.canvas.update()

    def fnCalendar(self, date_var):
        parent = ()
        self.tkCalendar(parent, self.year, self.month, self.day, date_var)

    def create_project_window(self):
        self.counter += 1
        projWin = tk.Toplevel(self)
        projWin.geometry('425x340+400+260')
        projWin.wm_title("Create Project")
        root.withdraw() #hide parent window
        date_var1 = StringVar(projWin)
        date_var1.set(self.strdate)
        
        tk.Label(projWin, text="Project Name:").grid(row=0, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Description:").grid(row=1, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Owner ID:").grid(row=2, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Associated Tasks:").grid(row=3, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Task Name:").grid(row=4, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Task Due Date:").grid(row=5, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Add Project Viewers:").grid(row=7, column=0, padx=6, pady=6, sticky=W)
        tk.Label(projWin, text="Viewer ID:").grid(row=8, column=0, padx=6, pady=6, sticky=W)
        
        projWin.e1 = Entry(projWin)
        projWin.e2 = Entry(projWin)
        projWin.e3 = Entry(projWin)
        projWin.e4 = Entry(projWin)
        projWin.e5 = Entry(projWin, textvariable=date_var1, bg="white", fg="blue", justify="center")
        projWin.e6 = Entry(projWin)

        projWin.e1.grid(row=0, column=1, padx=6, pady=6, sticky=W)
        projWin.e1.focus_set()
        projWin.e2.grid(row=1, column=1, padx=6, pady=6, sticky=W)
        projWin.e3.grid(row=2, column=1, padx=6, pady=6, sticky=W)
        projWin.e4.grid(row=4, column=1, padx=6, pady=6, sticky=W)
        projWin.e5.grid(row=5, column=1, padx=6, pady=6, sticky=W)
        
        projWin.calButton = tk.Button(projWin, text='Select Date', bg='#7fff00', relief=RAISED, command=lambda: self.fnCalendar(date_var1))
        projWin.calButton.grid(row=6, column=1, padx=6, pady=6, sticky=W)
        projWin.e6.grid(row=7, column=1, padx=6, pady=6, sticky=W)

        def commit_task():
            print("projWin task commit")
            #add task to project
            self.create_task_window()

        def commit_viewer():
            print("commit viewer")
            #add viewer to list

        def commit_project():
            #bring main window back
            root.update()
            root.deiconify()

            print("commit project")
            projWin.destroy()
            #add project to dictionary

            
        projWin.taskButton = tk.Button(projWin, text="Add Task", command=commit_task)
        projWin.taskButton.grid(row=5, column=2, padx=6, pady=6, sticky=W)
        projWin.viewerButton = tk.Button(projWin, text="Add Viewer", command=commit_viewer)
        projWin.viewerButton.grid(row=7, column=2, padx=6, pady=6, sticky=W)

        projWin.acceptButton = tk.Button(projWin, text="Accept", command=commit_project)
        projWin.cancelButton = tk.Button(projWin, text="Cancel", command=projWin.destroy)
        projWin.acceptButton.grid(row=8, column=0, padx=6, pady=6, sticky=W)
        projWin.cancelButton.grid(row=8, column=1, padx=6, pady=6, sticky=W)





if __name__ == "__main__":
    root = tk.Tk()
    #set main window size and placement according to screen size
    #rootsize tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    #root.geometry('900x400+40+80' % (rootsize + (()))
    app = Application(root)
    root.wm_title('Welcome to Task Commander BETA!')
    app.mainloop()

#Scroll bars
#http://www.gossamer-threads.com/lists/python/python/13135
#http://grokbase.com/t/python/python-list/99a67px8z7/tkinter-scrollable-buttons
#http://effbot.org/tkinterbook/scrollbar.htm

import getpass 
import datetime
import hashlib
import uuid
import string 
import shelve 
import sys

from pprint import pprint # for debugging ("pretty print" dicts and lists)

def hash_password(passwordpar):
	salt = uuid.uuid4().hex
	return hashlib.sha256(salt.encode() + passwordpar.encode()).hexdigest() + ':'+ salt
def check_password(hashed_passwordpar, user_passwordpar):
	password, salt = hashed_passwordpar.split(':')
	return password == hashlib.sha256(salt.encode() + user_passwordpar.encode()).hexdigest()

def DeleteProject(someUser, projectName):
	if projectName in someUser.projects[projectName]:
		del someUser.projects[projectName]

def createTask(projectName): ###make task start date the same as project start date, make project end date inferred from task end date
    name = raw_input("Enter the name of the task")
    projectName.addTask(name)
    description = raw_input("Enter a short description of the task")
    projectName.tasks[name].setDescription(description)
    start = raw_input("Enter the start date for the task")
    if start == "":
    	start = str(datetime.date.today())
    projectName.tasks[name].setStartDate(start)
    end = raw_input("Enter the deadline for the task")
    if end > projectName.getEndDate(): # if task end date is later than project end date,
        projectName.setEndDate(end) # update project's end date
    projectName.tasks[name].setTaskEndDate(end)

def DeleteTask(projectName, taskName): #!!!
	if taskName in projectName.tasks:
		del projectName.tasks[taskName]

class Users:
	def __init__(self, name):
		self.name = name
		self.users = {}

	def returnProgramtoPastState(self):
		self.users = shelve.open('taskcommanderS')
		print("DEBUG: USERS = {}".format(pprint(self.users)))
		
	def addUser(self, firstname, lastname, birthdate, userID, accessStatus): 
		self.users[userID] = User(firstname, lastname, birthdate, userID, accessStatus)

	def saveProgramInformation(self):
		self.taskcommanderS = shelve.open('taskcommanderS')
		listkeys = list(self.users.keys())
		listvalues = list(self.users.values())
		i = 0
		numberofusers = len(self.users)
		while (i < numberofusers):
			print("DEBUG: STORING {k} AS VALUE {v}".format(k=listkeys[i], v=listvalues[i]))
			self.taskcommanderS[listkeys[i]] = listvalues[i]
			i += 1
		#for (key, val) in self.users:
		#	self.taskcommanderS[key] = val
		self.taskcommanderS.close()

	def printdb(self):
		self.taskcommanderS = shelve.open('taskcommanderS')
		print(self.taskcommanderS)

#	def __repr__(self):
#		return (self.name, self.users)

SessionOne = Users('Session_One')

class User:
	def __init__(self, firstname, lastname, birthdate, userID, accessStatus):
		self.firstname = firstname
		self.lastname = lastname
		self.birthdate = birthdate
		self.userID = userID
		self.accessStatus = accessStatus
		self.projects = {}
		self.password = ""
		self.userName = ""
	def addProject(self, projectName):
		self.projects[projectName] = Project(projectName)
	def setUserName(self, userName_par):
		self.userName = userName_par
	def getUserName(self):
		return self.userName
	def setPassword(self, password): #for some reason password isn't being encrypted here, and encrypted password has been overwritten in database with plaintext password
		self.password = password
	def getPassword(self):
		return self.password
	def __repr__(self):
#		return "!".join(map(lambda x: str(x), [self.name, self.birthdate, self.userID, self.accessStatus, self.projects, self.userName_par, self.password, self.hashedpassword]))
		return "User({f}, {l}, {b}, {id}, {acc})".format(f=self.firstname, l=self.lastname, b=self.birthdate, id=self.userID, acc=self.accessStatus)
class Project:
	def __init__(self, name):
		self.name = name
		self.tasks = {}
		self.userscanview = []
	def addTask(self, taskName):
		self.tasks[taskName] = Task(taskName) #can't have duplicate task names in same project 
	def setProjectManager(self, ProjectManager):
		self.ProjectManager = ProjectManager
	def getProjectManager(self):
		return self.ProjectManager
	def setDescription(self, ProjectDescription):
		self.description = ProjectDescription
	def setStartDate(self, startdate):
		self.startdate = startdate
	def getStartDate(self):
		return self.startdate
	def setEndDate(self, enddate):
		self.enddate = enddate
	def getEndDate(self):
		return self.enddate
	def addUsercanview(self, userID):
		self.userscanview.append(userID)
#	def __repr__(self):
#		return "!".join(map(lambda x: str(x), [self.name, self.tasks, self.description, self.startdate, self.enddate, self.ProjectManager]))
class Task:
	def __init__(self, name):
		self.name = name
		self.completion = False
	def setDescription(self, TaskDescription):
		self.description = TaskDescription
	def setStartDate(self, startdate):
		self.startdate = startdate
	def getTaskStartDate(self):
		return self.startdate
	def setTaskEndDate(self,enddate):
		return self.enddate
#	def __repr__(self):
#		return "!".join(map(lambda x: str(x), [self.name, self.completion, self.description, self.startdate, self.enddate]))

def hash_password(passwordpar):
	salt = uuid.uuid4().hex
	return hashlib.sha256(salt.encode() + passwordpar.encode()).hexdigest() + ':'+ salt

def check_password(hashed_passwordpar, user_passwordpar):
	print(r"DEBUG: {}".format(hashed_passwordpar))
	password, salt = hashed_passwordpar.split(':')
	return (password == hashlib.sha256(salt.encode() + user_passwordpar.encode()).hexdigest())

def DeleteProject(someUser, projectName):
	if projectName in someUser.projects[projectName]:
		del someUser.projects[projectName]

def createTask(projectName): ###make task start date the same as project start date, make project end date inferred from task end date
    name = input("Enter the name of the task")
    projectName.addTask(name)
    description = input("Enter a short description of the task")
    projectName.tasks[name].setDescription(description)
    start = input("Enter the start date for the task")
    if start == "":
        start = str(datetime.date.today())
    projectName.tasks[name].setStartDate(start)
    end = input("Enter the deadline for the task")
    if end > projectName.getEndDate(): # if task end date is later than project end date,
        projectName.setEndDate(end) # update project's end date
    projectName.tasks[name].setTaskEndDate(end)

def DeleteTask(projectName, taskName): #!!!
	if taskName in projectName.tasks:
		del projectName.tasks[taskName]


def mainMenu(userid):    #general format for interacting with the database
	status = ''
	someUser = SessionOne.users[userid]  #1
	while (status != 'q'):
		print("Welcome to Task Commander")
		status = input("Enter (c) to create a new project and (s) to select an existing project.")
		if (status == 'c'):
			name = input("Enter the name of your project")
			someUser.addProject(name)
			description = input("Enter a short description of your project")
			someUser.projects[name].setDescription(description)
			start = input("Enter the start date for the project")
			if start == " ": 
				start = str(datetime.date.today())
			someUser.projects[name].setStartDate(start)
			end = input("Enter the end date for the project")
			someUser.projects[name].setEndDate(end)
			identification = input("Confirm user id")
			someUser.projects[name].setProjectManager(identification)
		elif (status == 's'):
			print(list(someUser.projects.keys()))
			active_project = input("Select the active project")
			if (someUser.userID == someUser.projects[active_project].getProjectManager()):
				PMdisplay(active_project, someUser.userID)
				sys.exit(0)
			else:
				viewDisplay(active_project, someUser.userID)
		elif (status == 'q'):
			break
		else:	
			print("Please enter a valid input")
	SessionOne.users[userid] = someUser #2
	SessionOne.saveProgramInformation()	#3

def viewDisplay(projectname, userID):
	someProject = SessionOne.users[userID].projects[projectname]
	print(someProject.name)
	print(someProject.getdescription())
	print(someProject.tasks)
	activetask = input("select task to complete")
	someProject[activetask].completion = True

def PMdisplay(projectname, userID):
	print(SessionOne.users[userID].projects[projectname])
	someProject = SessionOne.users[userID].projects[projectname]
	print("Welcome to the Display.")
	print(someProject.name)
	print(someProject.ProjectManager)
	print(someProject.tasks)
	print(someProject.userscanview)
	print(someProject.getEndDate())
	print(someProject.getStartDate())
	status = ''
	while (status != 'q'):
		status =input("(a) add task. (d) delete task. (e) edit dates (f) add user (g) see project completion")
		if (status == 'a'):
			createTask(someProject)
		elif (status == 'd'):
			DeleteTask(someProject)
		elif (status == 'e'):
			startdate = input("Enter new start date")
			someProject.setStartDate(startdate)
			enddate = input("Enter new end date")
			someProject.setEndDate(enddate)
		elif (status == 'f'):
			newuser = input("Enter user id of user who can view")
			someProject.addUsercanview(newuser)
			users[newuser].projects[projectname] = someProject  #this should add project as view only to specified user
		elif (status == 'g'):
			totaltasks = len(someProject.tasks)
			completetasks = [k for k, v in someProject.tasks.items() if v.completion]
			numbercomplete = len(completetasks)
			percentagecomplete = numbercomplete/totaltasks
			print(percentagecomplete)

		elif (status == 'q'):
			print(someProject.name)
			print(someProject.ProjectManager)
			print(someProject.tasks)
			print(someProject.userscanview)
			print(someProject.getEndDate())
			print(someProject.getStartDate())
			someUser = SessionOne.users[userID]
			someUser.projects[projectname] = someProject
			SessionOne.users[userID] = someUser 
			print(SessionOne.users[userID].projects[projectname].getStartDate())
			SessionOne.saveProgramInformation()
			sys.exit(0)
		else:
			print('Please enter valid input')


def login():
	status = ''
	while (status != 'q'):
		status = input("Are you an existing user? Enter (y/n). Press (q) to quit")
		if status == "y":
			SessionOne.returnProgramtoPastState()
			username = input("Enter username")
			userid = input("Enter userid")
			print (SessionOne.users[userid].getPassword()) #DEBUG
			expassword = getpass.getpass()
			print("DEBUG: PASSWORD = {}".format(SessionOne.users[userid].getPassword()))
			if (check_password(SessionOne.users[userid].getPassword(), expassword)): #still making calls to the database but not recognizing user attribute password!
				mainMenu(userid)
			break
		elif status == 'n':
			fname = input("Enter your first name")
			lname = input("Enter your last name")
			birthdate = input("Enter your birthdate 'MM/DD/YYYY")
			Uid = input("Enter your user identification number")
			if Uid in SessionOne.users:
				print('user identification number already exists')
				#allow them to either delete existing entry or to see what username and password is 
				break
			status = input("Select (A) for administrator and (U) for user")
			SessionOne.addUser(fname, lname, birthdate, Uid, status)
			username = input("Set your username (you may edit this later): ")
			SessionOne.users[Uid].setUserName(username)
			cpassword = getpass.getpass()
			cpassword = hash_password(cpassword)
			print(cpassword)
			SessionOne.users[Uid].setPassword(cpassword)
#			pprint("DEBUG: SESSIONONE = {}".format(SessionOne))
			SessionOne.printdb()
			SessionOne.saveProgramInformation()
if __name__ == "__main__":
	login()

import getpass 
import time
import hashlib
import uuid
import string 


def hash_password(passwordpar):
	salt = uuid.uuid4().hex
	return hashlib.sha256(salt.encode() + passwordpar.encode()).hexdigest() + ':'+ salt


def check_password(hashed_passwordpar, user_passwordpar):
	password, salt = hashed_passwordpar.split(':')
	return password == hashlib.sha256(salt.encode() + user_passwordpar.encode()).hexdigest()

class User:
	def __init__(self, name, birthdate, userID, accessStatus):
		self.name = name
		self.birthdate = birthdate
		self.userID = userID
		self.accessStatus = accessStatus
		self.projects = {}
	def addProject(self, projectName):
		self.projects[projectName] = Project(projectName)
	def setUserName(self, userName_par):
		self.userName_par = userName_par
	def getUserName(self):
		return userName
	def setPassword(self, password):
		self.password = password
	def getPassword(self):
		return self.password
class Project:
	def __init__(self, name):
		self.name = name
		self.tasks = {}
	def addTask(self, taskName):
		self.tasks[taskName] = Task(taskName) #can't have duplicate task names in same project 
	def setDescription(self, ProjectDescription):
		self.description = ProjectDescription
	def setStartDate(self, startdate):
		self.startdate = startdate
	def setEndDate(self, enddate):
		self.endate = enddate
class Task:
	def __init__(self, name):
		self.name = name
		self.completion = False


def CreateProject(someUser):
	name = raw_input("Enter the name of your project")
	someUser.addProject(name)
	description = raw_input("Enter a short description of your project")
	someUser.projects[name].setDescription(description)
	start = raw_input("Enter the start date for the project") #can automate this
	someUser.projects[name].setStartDate(start)
	end = raw_input("Enter the end date for the project")
	someUser.projects[name].setEndDate
def DeleteProject(someUser, projectName):
	if projectName in someUser.projects[projectName]:
		del someUser.projects[projectName]
def AddTask(someProject, taskName):
	someProject.tasks[taskName]= task(taskName)
def CompleteTask(someProject, taskName):
	someProject.tasks[taskName].completion = True
def DeleteTask(someProject, taskName):
	if taskName in someProject.tasks[taskName]:
		del someProject.tasks[taskName]


def login():
	users = {}
	l = []
	status = ''
	while (status != 'q'):
		status = raw_input("Are you an existing user? Enter (y/n). Press (q) to quit")
		if (status == 'y'):
			username = raw_input("Enter username")
			expassword = getpass.getpass()
			if (check_password(hashedPass, expassword)):
				l.append(newUser)
				break 
			else:
				break
		elif (status == 'n'):
			name =raw_input("Enter your full name")
			birthdate =raw_input("Enter your birthdate 'MM/DD/YYYY")
			Uid = raw_input("Enter your user identification number")
			status = raw_input("Select (A) for administrator and (U) for user")
			newUser = User(name, birthdate, Uid, status)
			username = raw_input("Set your username (you may edit this later): ")
			newUser.setUserName(username)
			password = getpass.getpass()
			hashedPass = hash_password(password)
			newUser.setPassword(hashedPass)
	return l 

def mainMenu(someUser):
	status = ''
	while (status != 'q'):
		print("Welcome to Task Commander")
		status = raw_input("Enter (c) to create a new project and (s) to select an existing project. Select (q) to quit")
		if (status == 'c'):
			CreateProject(someUser)
		if (status == 's'):
			print someUser.projects.keys()
			active_project = raw_input("Select the active project")
			break
	return someUser.projects[active_project]


display_result = mainMenu()

def display(display_result):
	status = ' '
	while (status != q):
		print("Enter (e) to edit project. Enter (a) to add new task. Enter (d) to delete existing task. Enter (c) to complete a task.\n")
		print("Enter (v) to view completed tasks. Enter (t) to edit task")
		if (status == 'e'):
			

result = login()
if result != []:
	mainMenu(result[0])
else:
	print("login not successful")



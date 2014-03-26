import time

class User:
	def __init__(self, name, userID):
		self.name = name
		self.userID = userID
		self.projects = {}
	def addProject(self, projectName):
		self.projects[projectName] = Project(projectName) #only problem with this is you can't name projects the same thing

class Project:
	def __init__(self, name):
		self.name = name
		self.tasks = {}
	def addTask(self, taskName):
		self.tasks[taskName] = Task(taskName) #can't have duplicate task names in same project 
	def setDescription(self, ProjectDescription):
		self.description = ProjectDescription


class Task:
	def __init__(self, name):
		self.name = name
		self.completion = False



username = raw_input("Enter username: ")
IDtag = raw_input("Enter ID: ")
newUser = User(username, IDtag)
s = raw_input("Enter (c) if you would like to create a new project or\n (s) if you would like to select an existing project and create new task\n")
if (s == 'c'):
	projectN = raw_input("Enter name of Project: ")
	newUser.addProject(projectN)
	UserProject = newUser.projects[projectN]
	projectD = raw_input("Enter description of Project: ")
	UserProject.setDescription(projectD)
	t = raw_input"Add tasks, enter (Q) when finished \n"
	while (t != "Q"):
		taskN = raw_input("Enter task name: ")
		UserProject.addTask(taskN)
		ProjectTask = UserProject.tasks[taskN]


	
	d = raw_input("Enter tasks for your new project, once finished enter (D)\n")
	while (d != "D"):
		newUserProject.addTask

elif (s == 's'):
	print newUser.projects.values()
else:
	print "Please enter a valid input"


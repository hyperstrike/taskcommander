import getpass 
import datetime
import hashlib
import uuid
import string 
import shelve 
import sys


class Users: #this is the information expert, look up information expert design pattern 
	def __init__(self, name):
		self.name = name
		self.users = {}

	def returnProgramtoPastState(self):
		self.users = shelve.open('taskcommanderS')

	def addUser(self, name, birthdate, userID, accessStatus):
		self.users[userID] = User(name, birthdate, userID, accessStatus)

	def saveProgramInformation(self):
		self.taskcommanderS = shelve.open('taskcommanderS')
		listkeys = self.users.keys()
		listvalues = self.users.values()
		i = 0
		numberofusers = len(self.users)
		while (i < numberofusers):
			self.taskcommanderS[listkeys[i]] = listvalues[i]
			i += 1
		self.taskcommanderS.close()

	def printdb(self):
		self.taskcommanderS = shelve.open('taskcommanderS')
		print (self.taskcommanderS)


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
		self.hashedpassword = hash_password(password)
	def getPassword(self):
		return self.hashedpassword
	def __repr__(self):
		return self.name

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
		self.users[userID].addProject(Project(self.name))
	def __repr__(self):
		return self.name

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
	def __repr__(self):
		return self.nam

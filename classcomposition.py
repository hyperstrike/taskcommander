from datetime import datetime
time = datetime()
#core idea here is that the user class contains projects and that the project class contains tasks
#we make project id's unique by appending the administrator-given user id to the date/time (even handles concurrent users!)
class User:
	def __init__(self, name, userID):
		self.name = name
		self.userID = userID
		self.projects = {}
	def addProject(self, projectName):
		projects[userID + makeProjectID()] = project(projectName) #project(name) is instantiation of project constructor contained in user class


class Project:
	def __init__(self, name):
		self.name = name
		self.tasks = {}
	def makeProjectID(self):
		return str(time.days, time.month, time.minutes, time.seconds, time.microseconds)
	def addTask(self, taskName):
		tasks[userID + makeProjectID()+ makeTaskID()]= task(taskName)

class Task:
	def __init__(self, name):
		self.name = name
		self.completion = False

	def makeTaskID(self):
		return str(time.days, time.month, time.minutes, time.seconds, time.microseconds)


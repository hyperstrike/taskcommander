import getpass 
import datetime
import hashlib
import uuid
import string 
import shelve 
import sys

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

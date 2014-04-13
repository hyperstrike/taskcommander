import model
import modelutilities
import view 

#as of now we have only worked on communication from view -> model, need to set up communication from model ->view

users = users("Session One")
#instantiate users and pass userid 
class CreateAccount:
	def __init__(self):
		self.firstname = MainWindow.getFirstName()
		self.lastname = MainWindow.getLastName()
		self.userID = MainWindow.getEmployeeID()
		#need to add something in view with accessStatus 
		self.birthdate = MainWindow.getDOB()
	def addUser(self): 
		users.addUser(firstname, lastname, userID, birthdate))

class Login: 
	def __init__(self):
		self.username = MainWindow.getUserName()
		self.password = MainWindow.getPassword()
		self.userID = #field from view with user identification 
		self.hashedpassword = users[userID].getpassword()

	def validate_password(self):
		check_password(self.hashedpassword, self.userpassword)
		#if true have view navigate to main menu, if false have view say invalid 

class CreateProject: #needs user ID from Login
	def __init__(self):
		self.name = #field from view with Project Name Entered 
		self.description = #field from view with Project Description Entered
		self.startdate = #field from view with Start Date Entered
		self.enddate = #field from view with End Date Entered
		self.usercanview = #will have to do something with this so 
	def CreateProject:
		CreatedProject = users[Login.userID].addProject(self.name)
		CreatedProject.setdescription(self.description)
		CreatedProject.setprojectmanager(User.userID)
		CreatedProject.setstardate(self.startdate)
		CreatedProject.setenddate(self.enddate)

class SelectProject: #all going to be information from model -> view
	def __init__(self):
		self.projects = users[Login.userID].projects.keys()
		self.selectedproject = #information from view on which project was selected, get information from model on that project
	def DisplayProjectNames:
		for i in range (0, len(self.projects)):
			#print project name to something in view
	


class EditProject: #all going to be information from model -> view

class CreateTask: #needs user ID from Login and Project Name from CreateProject
	def __init__(self):
		self.name = #field from view with Task Name entered
	def CreateTask:
		CreatedTask = users[Login.userID].projects[CreateProject.name]
		Users[CreateAccount.userID].projects[CreateProject.name].addTask(self.name)




		

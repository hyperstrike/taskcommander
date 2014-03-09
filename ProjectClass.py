import Task
# Look into pickling in Python

class Project:
    #Initial coding of the Project class for CPSC 362
    #__slots__ = {'_name', '_startDate', '_deadline', '_description', '_PMID', '_GAID', '_ProjectID', '_completionStatus', '_taskList', '_nextTaskID'}
    
    def __init__(self, ProjMan_ID, GlobAdmin_ID, newProjectID):
        self._PMID = ProjMan_ID #ID of the Project Manager that created (and can administor) the project.
        self._GAID = GlobAdmind_ID #Store the ID of the global admin

        self._ProjectID = newProjectID
#This assumes that the process that generates Project ID's is stored and runs elsewhere
#I was thinking that the outer program will pass in a generated ID during creation

        self._completionStatus = False #Project starts off not finished
        self._taskList = []
        self._nextTaskID = 0

    def get_project_name(self):
        return self._name

    def set_project_name(self, newName):
        self._name = newName

    def view_start_date(self):
        return self._startDate

    def set_start_date(self, newStartDate):
        self._startDate = newStartDate

    def view_project_deadline(self):
        return self._deadline

    def set_project_deadline(self, newDeadline):
        self._deadline = newDeadline

    def view_project_description(self):
        return self._description

    def write_project_description(self, newDescription):
        self._description = newDescription

    def get_project_ID(self):
        return self._ProjectID

    def get_PMID(self):
        return self._PMID

    def get_next_task_ID(self):
        #Increment and return the ID Number of the next task
        self._nextTaskID += 1
        return self._nextTaskID

    def is_user_ID_PM(self, user_ID):
        if user_ID == get_PMID():
            return True
        return False

    def get_completion_percent(self):
        return self._compPercent

    def set_completion_percent(self, newCompPercent):
        self._compPercent = newCompPercent

    def create_task(self):
        T_PMID = get_PMID()
        T_ProjectID = get_project_ID()
        TaskID = get_next_task_ID()
        newTask = Task(T_PMID, T_ProjectID, TaskID)
        taskList.append(newTask)

    def update_project_status(self):
        

    #def is_project_complete(self):

    projectDescription = property(write_project_description, view_project_description)
    projectDeadline = property(set_project_deadline, view_project_deadline)
    startDate = property(set_start_date, view_start_date)
    projectName = property(set_project_name, view_project_name)

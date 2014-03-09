class Task:
	#Initial coding of the Task class for CPSC 362
	__slots__ = {'_task_name', '_task_description', '_task_start_date', '_task_deadline''_T_PMID', '_T_ProjectID', '_TaskID', '_T_complete'}
	
	def __init__(self, ProjMan_ID, ProjectID, newTaskID):
		self._T_PMID = ProjMan_ID #ID of the Project Manager that
		#created and can edit and monitor the task
		self._T_ProjectID = ProjectID #ID of the affiliated Project
		self._TaskID = newTaskID #This assumes that the affiliated
		#Project will pass in a generated ID for the task
		self._T_complete = False #Initially, task is not finished
		
	def set_task_name(self, newTaskName):
		self._task_name = newTaskName
		
	def view_task_name(self):
		return self._task_name
		
	def write_task_description(self, newTaskDescription):
		self._task_description = newTaskDescription
		
	def view_task_description(self):
		return self._task_description
		
	def set_task_start_date(self, newTaskStart):
		self._task_start_date = newTaskStart
		
	def view_task_start_date(self):
		return self._task_start_date
		
	def set_task_deadline(self, newTaskDeadline):
		self._task_deadline = newTaskDeadline
		
	def view_task_deadline(self):
		return self._task_deadline
		
	def view_task_receivers(self, listOfTaskReceivers):
		for person in listOfTaskReceivers:
			print(person)
			
	def delegate_task_to_new_receiver(self, listOfTaskReceivers, newTaskReceiver):
		listOfTaskReceivers.append(newTaskReceiver)
			
	def set_task_as_complete(self):
		self._T_complete = True
		
	def is_task_complete(self):
		return self._T_complete
		
	taskDescription = property(write_task_description, view_task_description)
	taskDeadline = property(set_task_deadline, view_task_deadline)
	taskStartdate = property(set_task_start_date, view_task_start_date)
	taskName = property(set_task_name, view_task_name)
from Task import Task

class TaskManager():
    taskList = {} #Empty dictionary that will contain the objects' tasks
    
    #Constructor initializes an empty dictionary.
    def __init__(self):
        self.taskList = {}
    
    #Add a new object task in the list of objects
    def AddTask(self, task):
        self.taskList[len(self.taskList)+1] = task
        
    #List the attributes of the objects in the dictionary.
    def ViewTasks(self):
        for id, task in self.taskList.items():
            print('--- Tasks ---')
            print (f'{id}.\tTask Name: {task.getName()}')
            print (f'\tDescription: {task.getDescription()}')
            print (f'\tDue Date: {task.getDueDate()}')
            print (f'\tPriority: {task.getPriority()}')
     
    #Update the attributes of the objects in the dictionary.
    #Args: idToUpdate: ID of the task that must be updated 
    #      attributeToUpdate: Attribute to be updated       
    #      newValue: New value for the attribute.         
    def UpdateTask(self, idToUpdate, attributeToUpdate, newValue):
        for id, task in self.items():
            if idToUpdate == id:
                match attributeToUpdate:
                    case 1:
                        task.setName(newValue)
                    case 2:
                        task.setDescription(newValue)
                    case 3:
                        task.setDueDate(newValue)
                    case 4:
                        task.getPriority(newValue)

    #Delete the objects in the dictionary.
    #Args: idToUpdate: ID of the task that must be deleted
    def DeleteTask(self, idToDelete):
        self.taskList.pop(idToDelete)
        
    
        

        
            
        
        
        
        
    
    
from Task import Task

class TaskManager():
    taskList = {} #Empty dictionary that will contain the objects' tasks
    
    #Constructor initializes an empty dictionary.
    def __init__(self):
        self.taskList = {}
    
    #Add a new object task in the list of objects
    #Args: task: Object that will be added to the dictonary 
    def AddTask(self, taskName,taskDescription,taskDueData,taskPriority):
        try:
            task = Task(taskName,taskDescription,taskDueData,taskPriority)
            self.taskList[len(self.taskList)+1] = task
            print('Task Added successfully!')
        except ValueError:
            print('Type of data entered not accepted by the application!')
        except:
            print('Something else went wrong')
                  
    #Display the attributes of the objects in the dictionary.
    def ViewTasks(self):
        for id, task in self.taskList.items():
            print (f'{id}.\tTask Name: {task.getName()}')
            print (f'\tDescription: {task.getDescription()}')
            print (f'\tDue Date: {task.getDueDate()}')
            print (f'\tPriority: {task.getPriority()}')
            
            
    #Update the attributes of the objects in the dictionary.
    #Args: idToUpdate: ID of the task that must be updated 
    #      attributeToUpdate: Attribute to be updated       
    #      newValue: New value for the attribute.         
    def UpdateTask(self, idToUpdate, attributeToUpdate, newValue):
        try:
            for id, task in self.taskList.items():
                if idToUpdate == id:
                    match attributeToUpdate:
                        case 1:
                            task.setName(newValue)
                        case 2:
                            task.setDescription(newValue)
                        case 3:
                            task.setDueDate(newValue)
                        case 4:
                            task.setPriority(newValue)
            print('Task updated successfully!')
        except ValueError:
            print('Type of data entered not accepted by the application!')
        except:
            print('Something else went wrong')

    #Delete the objects in the dictionary.
    #Args: idToDelete: ID of the task that must be deleted
    def DeleteTask(self, idToDelete):
        self.taskList.pop(idToDelete)
        
    def IsTaskListEmpty(self):
        return bool(self.taskList)    
    
        

        
            
        
        
        
        
    
    
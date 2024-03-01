from TaskManager import TaskManager

taskManager_1 = TaskManager()

def skipTwoLines():
    print('')
    print('')

#Function to be used when it's necessary to get the user option from the list     
def userChoiceFunction():
    return int(input('Enter your choice: '))
    
print('Welcome to Task Manager')
skipTwoLines()
print('1. Add Task')
print('2. View Task')
print('3. Update Task')
print('4. Delete Task')
print('5. Exit Task')
skipTwoLines()
   
userChoice = userChoiceFunction()
while userChoice != 5: #Loop to keep the user in the application until they choose the value 5.
    match userChoice:
        case 1:
            taskName = input('Enter task name: ')
            taskDescription = input('Enter task description: ') 
            taskDueData = input('Enter due date (YYYY-MM-DD): ') 
            taskPriority = input('Enter priority (High/Medium/Low): ') 
            #Add a new object to the existing dictionary.
            taskManager_1.AddTask(taskName,taskDescription,taskDueData,taskPriority) 
            skipTwoLines()          
        case 2:
            print('--- Tasks ---')
            taskManager_1.ViewTasks()
            skipTwoLines()       
        case 3:
            if taskManager_1.IsTaskListEmpty():
                idToUpdate = int(input('Enter task ID to update: '))
                if taskManager_1.IsTaskInDictionary(idToUpdate):
                    print('Enter the number corresponding to the attribute to be updated:')
                    print('1 - Name / 2 - Description / 3 - Due date / 4 - Priority')
                    attributeToUpdate = int(input('Enter the number: '))
                    newValue = input('Enter new Value: ')
                    taskManager_1.UpdateTask(idToUpdate, attributeToUpdate, newValue)
                else:
                    print('There is no task with the ID informed!')
            else:
                print('There is no task to update.') 
            
            skipTwoLines()    
        case 4:
            if taskManager_1.IsTaskListEmpty():
                idToDelete = int(input('Enter task ID to delete: '))
                if taskManager_1.IsTaskInDictionary(idToDelete):
                    taskManager_1.DeleteTask(idToDelete)
                    print('Task deleted successfully!')
                else:
                    print('There is no task with the ID informed!')
            else:
                print('There is no task to delete.')      
            skipTwoLines() 
        case 5:
            pass
        case _:
            print('Invalid Choice!')
    userChoice = userChoiceFunction()

print('Exiting Task Manager. Goodbye!') 
        
    
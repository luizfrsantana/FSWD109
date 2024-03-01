from Task import Task
from TaskManager import TaskManager

taskManager_1 = TaskManager()
def space():
    print('')
    print('')
    
def userChoiceFunction():
    return int(input('Enter your choice: '))
    
print('Welcome to Task Manager')
space()
print('1. Add Task')
print('2. View Task')
print('3. Update Task')
print('4. Delete Task')
print('5. Exit Task')
space()   
userChoice = userChoiceFunction()
while userChoice != 5:
    match userChoice:
        case 1:
            taskName = input('Enter task name: ')
            taskDescription = input('Enter task description: ') 
            taskDueData = input('Enter due date: ') 
            taskPriority = input('Enter priority (High/Medium/Low): ') 
            taskManager_1.AddTask(Task(taskName,taskDescription,taskDueData,taskPriority))
            
            print('Task Added successfully!')
            space()          
        case 2:
            print('--- Tasks ---')
            taskManager_1.ViewTasks()
            space()       
        case 3:
            idToUpdate = int(input('Enter task ID to update: '))
            print('Enter the number corresponding to the attribute to be updated:')
            print('1 - Name / 2 - Description / 3 - Due date / 4 - Priority')
            attributeToUpdate = int(input('Enter the number: '))
            newValue = input('Enter new Value: ')
            taskManager_1.UpdateTask(idToUpdate, attributeToUpdate, newValue) 
            
            print('Task updated successfully!')
            space()    
        case 4:
            taskManager_1.DeleteTask(int(input('Enter task ID to delete: ')))
            print('Task deleted successfully!')
            space() 
        case 5:
            pass
        case _:
            print('Invalid Choice!')
    userChoice = userChoiceFunction()

print('Exiting Task Manager. Goodbye!') 
        
    
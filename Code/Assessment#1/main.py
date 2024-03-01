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
            space()          
        case 2:
            taskManager_1.ViewTasks()
            space()       
        case 3:
            pass   
        case 4:
            pass   
        case 5:
            pass   
        case _:
            print('Invalid Choice!')
    userChoice = userChoiceFunction()
    
print('Exiting Task Manager. Goodbye!')
        
    
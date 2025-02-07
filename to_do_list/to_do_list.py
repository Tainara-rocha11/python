# simple To Do List

tasks = []
#functions to add, list and remove tasks
def addTasks (task):
    tasks.append(task)
    print (f'Task add successfully!')
def listTasks():
    if not tasks:
        print('No tasks on the list!')
    else:
        print ('\n Task list: ')
        for i, task in enumerate(tasks,1):
            print (f'{i}. {task}')
def removeTask(number):
    if 1 <= number <= len(tasks):
        task_remove = tasks.pop(number - 1)
        print(f'Task {task_remove} removed successfully!')
    else: 
        print ('Invalid number try again!')
#interactive menu with available options
while True: 
    print ('''
    Options: 
    [1] Add Task
    [2] List Task 
    [3] Remove Task
    [4] To go out

''')
# conditionals
    option = int (input('Choose an option: '))
    if option == 1:
        task = input('Enter a new task: ')
        addTasks(task)
    elif option == 2:
        listTasks()
    elif option == 3:
        listTasks()
        number = int (input('Enter a task you want to remove: '))
        removeTask(number)
    elif option == 4:
        print ('Leaving the program. Thank you for using!')
        break
    else: 
        print ('Invalid option try again!')
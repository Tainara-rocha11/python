# Simple Calculator - python terminal

# declaring functions to perform mathematical operations
def add (num1,num2):
    return num1 + num2 

def substract (num1,num2):
    return num1 - num2

def multiply (num1,num2):
    return num1 * num2 

def division (num1, num2):
    return num1 / num2

# building the interaction menu

while True: 
    num1 = float (input('Enter a number: '))
    num2 = float (input('Enter another number: '))

    print ('''
    Available options
    
    [1] Addition 
    [2] Subtraction
    [3] Multiplication
    [4] Division
    [0] Exit.


''')
    option = int (input('Select an option: '))

# conditionals
    if option == 1:
        print (f'The sum of the numbers {num1} + {num2} was equal to', add(num1,num2))
    elif option == 2:
        print (f'The subtraction between the numbers {num1} - {num2} was equal to', substract(num1,num2))
    elif option == 3:
        print (f'The multiply between the numbers {num1} * {num2} was equal to', multiply(num1,num2))
    elif option == 4:
        print (f'The division between the numbers {num1} / {num2} was equal to', division(num1,num2))
    else: 
        print ('End of the program. Thank for using!')
        break


import random
import string 

def generator_passowrd(length=12):
    characteres = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characteres) for _ in range(length))

    return password

password_length = int (input('Enter the desired password length: '))

password = generator_passowrd(password_length)

print (f'Your generated password is: {password}')
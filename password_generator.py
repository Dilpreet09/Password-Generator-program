from string import punctuation, digits,ascii_letters
import random

print ("Welcome to the Password Generator program ---> Dilpreet Singh Kohli\n")

option = str(input("Please enter how strong you would like your password to be: (S - Strong) or (W- Weak): ")).capitalize()

password = []       #Empty string

if option  == 'S' or option == 'Strong':
    for x in range(0,10):
        combine = punctuation + digits + ascii_letters
        random_choice = random.choice(combine)
        password.append(random_choice)
    password = ''.join(password)
    print ("Generated Password: "+ password)
elif option  == 'W' or option == 'Weak':
    for x in range(0,6):
        combine = punctuation + digits + ascii_letters
        random_choice = random.choice(combine)
        password.append(random_choice)
    password = ''.join(password)
    print ("Generated Password: "+ password)
else:
    print("Incorrect Option\nTry Again!")




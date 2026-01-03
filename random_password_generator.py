#                                                               Task 2
'''inputs:
length
character types(letters,numbers and symbols)'''

# Code
import random #used to genarate the random letters
""""In random library we use 1 method to complete this task 2 i.e
    random.choice(characters) -> used to select the choices randomly for the available(may be numbers,letters or symbols)"""
import string 
"""There are many methods in string library but in our task 2 we just need 3 methods.
                1.string.ascii_letters -> prints random letters(small & caps combo)
                2.string.digits -> prints random numbers (0-9)
                3.string.punctuation -> used to print random symbols(!@#$%^&*()_+-=[]{}|;:'",.<>?/)"""
                
length = int(input("Enter your password length: "))
use_letters = input("Do you want to use letters in your password (y/n): ").lower()
use_numbers = input("Do you want to use numbers in your password (y/n): ").lower()
use_symbols = input("Do you want to use symbols in your password (y/n): ").lower()

#Buiding charcter sets

characters_set =""
if use_letters == "y":
    characters_set += string.ascii_letters
if use_numbers == "y":
    characters_set += string.digits
if use_symbols == "y":
    characters_set += string.punctuation
"""now the as all the above if statement satisfies the charcter set will contains
    character_set = abcDEF.....xyZ0123456789!@#$%^&*()_+-=[]{}|;:'",.<>?/"""

# Validation stage

if length <= 0:
    print("Enter valid length of your password.")
elif characters_set == "":
    print("Please, select atleast one charcter type i.e numbers or symbols or letters.")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters_set)
print(f"Your Generated password(random) is:{password}")


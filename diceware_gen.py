from diceware_dict import diceware_dict
import random

def dice(number):
    x = ""
    for i in range(number):
        x += str(random.randint(1, 6))
    return x
def password(words):
    password = ""
    for i in range(words):
        password += diceware_dict[dice(5)] + " "
    return password
print(password(int(input("enter the number of words you want in your password: "))))

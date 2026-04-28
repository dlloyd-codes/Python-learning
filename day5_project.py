#password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '£', '%', '*', '@', '+', '^']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


print("Welcome to the Password Generator!")
let_req = int(input("How many letters do you want in the password?"))
sym_req = int(input("How many symbols do you want in the password?"))
num_req = int(input("How many numbers do you want in the password?"))

password = ""

for char in range(0, let_req):
    password = password + random.choice(letters)

for char in range(0, sym_req):
    password = password + random.choice(symbols)

for char in range(0, num_req):
    password = password + random.choice(numbers)

password_list = list(password)

random.shuffle(password_list)

shuffled_password = ""
for char in password_list:
    shuffled_password += char

print(f"Your Final Password Is: {shuffled_password}")
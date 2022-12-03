import random

password_length = 12

characters = "abcde12345"

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))
input(" [+] Enter To Exit")

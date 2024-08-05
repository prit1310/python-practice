import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess number between 1 to 100 or Quit(Q):")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("your num is",target)
        break
    if(userChoice < target):
        print("your number is small, guess bigeer number")
    else:
        print("your number is big, guess small number")

print("Game Over !!!")





import random
import string

pass_len = 6
charVal = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password +=random.choice(charVal)

password = "".join([random.choice(charVal) for i in range(pass_len)])

print("Your random password is:",password)
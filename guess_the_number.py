import random
import sys


minnum = int(input("Enter the minimum you like: "))
maxnum = int(input("Enter the maximum you like: "))

n = random.randint(minnum, maxnum)

while n >= minnum:
    num = int(input("Guess the number: "))
    if num == n:
        print("Congratulations! You guessed the correct number.")
        break
    elif num < n:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
        


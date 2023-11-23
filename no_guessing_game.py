#number guessing game

import random
import sys

a=random.randint(1,100)
for i in range(5):
    n=int(input("Guess the number between 1 to 100 "))
    if(a>n):
        print(f"Generated number is greater than {n}")
    elif(a<n):
        print(f"Generated number is smaller than {n}")
    else:
        print("Great!! You got it right.")
        sys.exit()
print(f"Generated number is {a}")
print("Out of chances...Better luck next time.")

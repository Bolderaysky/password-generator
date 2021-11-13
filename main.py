from random import choice
from time import time

Symbols = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>"

def Generate(Length = 10):

    Password = ""
    TimeBefore = time()

    for i in range(Length):
        Password += choice(Symbols)
    TimeAfter = time()

    print(f"Your password is '{Password}' that was generated in {TimeAfter - TimeBefore} seconds.")



if __name__ == "__main__":
    try:
        Length = int(input("Type length of password:"))
        if Length <= 0:
            print("Password length can't be less than 1. Program will continue with length = 10.")
            Length = 10
        Generate(Length)
        input("\nPress any key to continue...")
    except:
        print("You've typed not an integer!")
        input()
        exit(-1)
        
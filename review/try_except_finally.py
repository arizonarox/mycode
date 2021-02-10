#!/usr/bin/python3

#what I hope will work!
try:
    num = int(input("Type in a number."))

#what is my contingency if it doesn't work
except:
    print("That was not a number!")
    num = "That wasn't a number!")

#whether it works or not, do this no matter what
finally:
    print("Thanks for using my script!")

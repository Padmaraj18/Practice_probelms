"""
Positive, Negative, or Zero Checker

Create a function named check_sign that accepts an integer
The function should print whether the number is positive, negative, or zero. """

def check_sign(num):
    if num > 0:
        print("It is a positive number ")
    elif num < 0:
        print("It is a negative number ")
    else:
        print(" it is a zero ")

check_sign(-8)
check_sign(8)
check_sign(0)

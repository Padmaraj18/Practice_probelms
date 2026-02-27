"""
Odd or Even Checker Function

---

**Problem:** Create a Python function named `check_number` that accepts a single integer 
parameter. The function should 
check whether the provided number is even or odd and then print the result.

"""

def check_number (num):
    if num % 2 == 0:
        print("it is a even number ")
    else:
        print("it is a odd number ")

check_number(2)

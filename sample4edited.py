"""
**List Manipulation**
---
**Problem:** 
Create a function named `remove_duplicates` that takes a list of numbers as input.
The function should remove any duplicate numbers from the list and return 
a new list with only unique numbers.
"""

def remove_duplicates(input_list):
    unique_set = set(input_list)
    return list(unique_set)

numbers = [2,2,3,4,5,5,3,4,6,7,8,9,9,6,7,8]

print(remove_duplicates(numbers))
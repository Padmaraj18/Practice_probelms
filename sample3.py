"""
List Filter 
---
**Problem:** 
Given a list of numbers, create a new list containing only numbers greater than 50.
"""

Original_list =  [25, 65, 40, 80, 15, 95]
def filter_numbers(data_list):
    filtered_list = []
    for num in data_list:
        if num > 50:
            filtered_list.append(num)
    return filtered_list

result = filter_numbers(Original_list)

print("original list", Original_list)
print("numbers greater than 50", result)
 
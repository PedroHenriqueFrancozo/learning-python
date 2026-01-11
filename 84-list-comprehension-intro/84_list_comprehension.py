"""
Lesson 84: Introduction to List Comprehension
List comprehension is a concise way to create lists from iterables.
It is generally faster and more 'Pythonic' than using traditional for loops.
"""

# Traditional way using for loop
numbers_list = []
for number in range(10):
    numbers_list.append(number)
print(f"Traditional: {numbers_list}")

# Using List Comprehension
# Structure: [expression for item in iterable]
lc_numbers = [number for number in range(10)]
print(f"List Comp:  {lc_numbers}")

# Applying logic: multiplication
# Here we multiply each number by 2 before adding it to the list
doubled_numbers = [
    number * 2 
    for number in range(10)
]
print(f"Doubled:    {doubled_numbers}")
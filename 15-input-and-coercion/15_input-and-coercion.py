"""
Topic: User Input and Type Conversion
Focus: Capturing data from the terminal and converting it to numbers.
"""

# The input() function always returns a string (str).
# name = input('What is your name? ')
# print(f'Your name is {name}')

number_1 = input('Enter a number: ')
number_2 = input('Enter another number: ')

# Coercion (type conversion) is necessary for mathematical operations
int_number_1 = int(number_1)
int_number_2 = int(number_2)

print(f'The sum of the numbers is: {int_number_1 + int_number_2}')
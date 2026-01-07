"""
Topic: Arithmetic Operators
Focus: Basic and advanced mathematical operations in Python.
"""

addition = 10 + 10
print('Addition:', addition)

subtraction = 10 - 5
print('Subtraction:', subtraction)

multiplication = 10 * 10
print('Multiplication:', multiplication)

division = 10 / 3  # Always returns a float
print('Division:', division)

integer_division = 10 // 3 # Discards the decimal part
print('Integer Division:', integer_division)

exponentiation = 2 ** 10
print('Exponentiation:', exponentiation)

modulo = 55 % 2  # Remainder of the division
print('Modulo (Remainder):', modulo)

# Practical Use of Modulo: Checking divisibility
print('Is 10 divisible by 8?', 10 % 8 == 0)
print('Is 16 divisible by 8?', 16 % 8 == 0)
print('Is 15 even?', 15 % 2 == 0) # False means it's odd
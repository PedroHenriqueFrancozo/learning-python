"""
Functions Exercises
1. Create a function that multiplies all unnamed arguments.
2. Create a function that checks if a number is even or odd.
"""

# 1. Multiplying arguments
def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

product = multiply(1, 2, 3, 4, 5)
print(f'Multiplication total: {product}')

# 2. Even or Odd
def is_even_or_odd(number):
    # Logic: if remainder of division by 2 is 0, it's even
    if number % 2 == 0:
        return f'{number} is Even'
    return f'{number} is Odd'

print(is_even_or_odd(10))
print(is_even_or_odd(15))
"""
Topic: Named and Unnamed (Positional) Arguments
Focus: Understanding how Python assigns values to parameters during function calls.
"""

# Function definition
def sum_values(x, y, z):
    # Using f'{x=}' is great for debugging: it shows both name and value
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# 1. Unnamed arguments (Positional)
# Values are assigned based on their order/position
sum_values(1, 2, 3)

# 2. Named arguments (Keyword Arguments)
# Values are assigned by the parameter name using the equals sign
sum_values(1, y=2, z=5)

# Practical example of a named argument in built-in functions:
# 'sep' is a named argument of the print function
print(1, 2, 3, sep='-')
"""
Topic: Basic String Interpolation
Focus: Using the % operator for string, int, float and hex formatting.
"""

# s - string
# d and i - int
# f - float
# x and X - Hexadecimal (ABCDEF0123456789)

name = 'Luiz'
price = 1000.95897643
# Interpolating name (string) and price (float with 2 decimal places)
variable = '%s, the price is $%.2f' % (name, price)
print(variable)

# Hexadecimal formatting
# %d for decimal, %08X for Hex with 8 digits and padding zeros
print('The hexadecimal of %d is %08X' % (1500, 1500))
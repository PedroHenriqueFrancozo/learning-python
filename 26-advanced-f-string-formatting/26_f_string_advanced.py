"""
Topic: Advanced String Formatting with f-strings
Focus: Alignment, padding, sign control, and conversion flags.
"""

# s - string
# d - int
# f - float
# .<number of digits>f
# x or X - Hexadecimal
# (Character)(><^)(quantity)
# > - Aligns to the right
# < - Aligns to the left
# ^ - Aligns to the center
# = - Forces the number sign to appear before padding zeros
# Sign - + or -
# Conversion flags - !r (calls __repr__), !s (calls __str__), !a (calls __ascii__)

variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}')      # Padding to the right
print(f'{variable: <10}.')     # Padding to the left
print(f'{variable: ^10}.')     # Centered
print(f'{1000.4873648123746:0=+10,.1f}') # Sign, padding, comma separator and precision
print(f'The hexadecimal of 1500 is {1500:08X}')
print(f'{variable!r}')         # Shows the raw value (with quotes)
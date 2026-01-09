"""
Topic: String Slicing
Focus: Understanding [start:stop:step] and the len() function.
"""

#  012345678
#  Olá mundo
# -987654321

# Slicing [start:stop:step] [::]
# Note: The len() function returns the character count of the string

variable = 'Olá mundo'

# Basic slicing: from index 4 to the end
print(variable[4:])

# Slicing with range: from 0 to 5 (stop index is not included)
print(variable[0:5])

# Slicing with step: every second character
print(variable[0:9:2])

# Reverse string (The "Pythonic" way)
print(variable[::-1])

# Using len()
print(f'The length of the string is: {len(variable)}')
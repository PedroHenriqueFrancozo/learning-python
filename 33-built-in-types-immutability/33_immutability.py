"""
Topic: Built-in types and Immutability
Focus: Understanding that types like str, int, float, and bool cannot be changed in place.
Reference: https://docs.python.org/3/library/stdtypes.html
"""

# Immutable types we've seen: str, int, float, bool
# Once created, you cannot change the internal value of these objects.

string = '1000'

# Attempting to change a character directly would raise an error:
# string[3] = 'A' # TypeError: 'str' object does not support item assignment

# To "change" it, we must create a new variable or reassign:
other_variable = f'{string[:3]}ABC{string[4:]}'

print(f"Original: {string}")
print(f"Modified (New object): {other_variable}")

# .zfill(n) - Useful built-in method to pad a string with zeros to the left
print(f"Zfill example: {string.zfill(10)}")
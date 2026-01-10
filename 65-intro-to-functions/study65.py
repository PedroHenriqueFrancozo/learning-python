"""
Topic: Introduction to functions (def) in Python 
Focus: Understanding how functions replicate actions, handle arguments, and return values.
"""

# Functions are snippets of code used to replicate 
# a specific action throughout your program.
# By default, Python functions return 'None'.

def greet(name):
    # 'name' is a parameter (a placeholder for the data)
    print(f'Hello, {name}!')

# Calling the function with different arguments
greet('Pedro')
greet('Ana')

# Calling with an empty string
greet('')

# Demonstrating the default return value (None)
result = greet('Alice')
print(f'The return value of the function was: {result}')
"""
Topic: Higher Order Functions and First-Class Functions
Focus: Handling functions as objects and passing them as arguments.
"""

def greet(message, name):
    return f'{message}, {name}!'

# 'execute' is a Higher Order Function
def execute(function, *args):
    # It takes a function and arguments, then runs it
    return function(*args)

# Passing the 'greet' function as a regular data object
print(execute(greet, 'Good morning', 'Luiz'))
print(execute(greet, 'Good night', 'Maria'))
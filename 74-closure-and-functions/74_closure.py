"""
Topic: Closure and functions that return functions
Focus: Lexical scoping and preserving state in Python functions.
"""

def make_greeting(greeting):
    # The inner function keeps access to the 'greeting' variable
    def greet(name):
        return f'{greeting}, {name}!'
    return greet

# Creating specialized functions (Closures)
say_good_morning = make_greeting('Good morning')
say_good_night = make_greeting('Good night')

names = ['Maria', 'Joana', 'Luiz']

for name in names:
    print(say_good_morning(name))
    print(say_good_night(name))
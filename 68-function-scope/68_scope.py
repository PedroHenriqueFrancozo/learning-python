"""
Topic: Function Scope in Python
Scope is the area where a specific name (variable) is accessible.
"""

x = 1  # Global scope variable

def outer_scope():
    global x  # Directs the function to use the 'x' from the global scope
    x = 10    # Modifies the global 'x'

    def inner_function():
        global x
        x = 11  # Modifies the global 'x' again
        y = 2   # Local scope variable (only exists inside here)
        print(f'Inside inner_function: {x=}, {y=}')

    inner_function()
    print(f'Inside outer_scope: {x=}')

print(f'Before function call: {x=}')
outer_scope()
print(f'After function call: {x=}')
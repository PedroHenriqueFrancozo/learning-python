"""
Topic: Default values for parameters
When defining a function, parameters can have default values.
If no value is sent for that parameter, the default is used.
"""

# Refactoring: editing code to be more flexible
def add(x, y, z=None):
    # Checking if z was provided (is not None)
    if z is not None:
        print(f'{x=} {y=} {z=}', '| Total:', x + y + z)
    else:
        print(f'{x=} {y=}', '| Total:', x + y)

add(1, 2)            # z defaults to None
add(3, 5)            # z defaults to None
add(7, 9, 0)         # z is explicitly 0
add(y=9, z=0, x=7)   # Using named arguments with default values
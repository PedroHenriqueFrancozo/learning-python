"""
Topic: Identity, Flags and None
Focus: Understanding 'id', 'is', 'is not' and the concept of 'None'.
"""

# Flag (Bandeira) - Marking a location/state in the code
# None = No value (used to initialize variables)
# is / is not = Checks identity and type (is it the same object in memory?)
# id = Identity (the memory address of the object)

condition = False
passed_in_if = None  # Using None as a flag

if condition:
    passed_in_if = True
    print('Doing something...')
else:
    print('Not doing something.')

# Using 'is None' to check if the variable was never modified
if passed_in_if is None:
    print('Did not pass in the if block')

if passed_in_if is not None:
    print('Passed in the if block')

# Demonstration of id
v1 = 'a'
v2 = 'a'
print(f'Memory ID of v1: {id(v1)}')
print(f'Memory ID of v2: {id(v2)}')
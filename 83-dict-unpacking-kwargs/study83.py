"""
Lesson 83: Dictionary Packing and Unpacking (**kwargs)
Packing: Gathering named arguments into a dictionary.
Unpacking: Spreading dictionary key-value pairs into a function or another dict.
"""

# 1. Swapping values (Basic unpacking)
a, b = 1, 2
a, b = b, a

# 2. Merging dictionaries using unpacking (**)
person = {
    'name': 'Aline',
    'last_name': 'Souza',
}

personal_data = {
    'age': 16,
    'height': 1.6,
}

# Creating a new dict by unpacking two existing ones
full_person_data = {**person, **personal_data}
print(f"Merged Dictionary: {full_person_data}")

# 3. Using *args and **kwargs in functions
def show_named_arguments(*args, **kwargs):
    print('NON-NAMED (args):', args)
    print('NAMED (kwargs):')
    for key, value in kwargs.items():
        print(f'  {key}: {value}')

# Passing arguments directly
print("\nDirect call:")
show_named_arguments(1, 2, name='Joana', job='Developer')

# Unpacking a dictionary into the function call
print("\nUnpacking call:")
config = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
}
show_named_arguments(**config)
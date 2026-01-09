"""
Topic: Operators 'in' and 'not in'
Focus: Checking for substrings and understanding iterables.
"""

# Strings are iterables
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# name = 'Otávio'
# print(name[2])
# print(name[-4])
# print('vio' in name)
# print('zero' in name)
# print(10 * '-')
# print('vio' not in name)
# print('zero' not in name)

name = input('Enter your name: ')
find = input('Enter what you want to find: ')

if find in name:
    print(f'{find} is in {name}')
else:
    print(f'{find} is not in {name}')
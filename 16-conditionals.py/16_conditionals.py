"""
Topic: Conditional Flow (if, elif, else)
Focus: Controlling the program flow based on user input.
"""

# if / elif      / else
# if / else if   / else
entry = input('Do you want to "enter" or "exit"? ')

if entry == 'enter':
    print('You have entered the system')
    print(12341234)
elif entry == 'exit':
    print('You have left the system')
else:
    print('You did not type enter or exit.')

print('OUTSIDE THE BLOCKS')
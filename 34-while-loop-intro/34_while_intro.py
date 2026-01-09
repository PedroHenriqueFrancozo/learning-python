"""
Topic: While Loop - Introduction
Focus: Executing actions while a condition is true and using 'break'.
"""

# Repetitions
# while (enquanto)
# Executes an action as long as a condition is true.
# Infinite Loop -> When the code has no end condition (or it never becomes false).

condition = True

while condition:
    name = input('What is your name? ')
    print(f'Your name is {name}')

    # 'break' is used to exit the loop immediately
    if name == 'exit' or name == 'sair':
        break

print('The loop has finished.')

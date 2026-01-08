"""
Exercise: Comparing two values
Focus: Practicing input, conditional logic, and f-string formatting.
"""

first_value = input('Enter a value: ')
second_value = input('Enter another value: ')

if first_value >= second_value:
    print(
        f'first_value={first_value} is greater than or '
        f'equal to second_value={second_value}'
    )
else:
    print(
        f'second_value={second_value} is greater '
        f'than first_value={first_value}'
    )

"""
Pro Tip: Using f-string debugging shortcut
print(f'{first_value=} is greater than {second_value=}')
The '=' inside the curly braces prints both the variable name and its value.
"""
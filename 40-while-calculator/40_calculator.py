"""
Topic: Calculator with while loop
Focus: Building a functional program with error handling and multiple conditions.
"""

while True:
    number_1 = input('Enter a number: ')
    number_2 = input('Enter another number: ')
    operator = input('Enter the operator (+ - / *): ')

    valid_numbers = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except Exception:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both numbers entered are invalid.')
        continue

    allowed_operators = '+-/*'

    if operator not in allowed_operators:
        print('Invalid operator.')
        continue

    if len(operator) > 1:
        print('Enter only one operator.')
        continue

    print('Calculating... Check the result below:')

    if operator == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operator == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operator == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operator == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        # Logical safeguard
        print('Something went wrong. This should not happen!')

    # Exit logic using string methods
    exit_prompt = input('Do you want to exit? [y]es: ').lower().startswith('y')

    if exit_prompt is True:
        break

print('Calculator closed.')
"""
Topic: Introduction to try/except
Focus: Error handling and preventing program crashes.
"""

# try -> attempts to execute the code
# except -> executed if an error occurs in the try block

number_str = input(
    'I will double the number you type: '
)

try:
    # Attempting to convert and print
    number_float = float(number_str)
    print(f'FLOAT: {number_float}')
    print(f'The double of {number_str} is {number_float * 2:.2f}')
except:
    # This block runs if the conversion fails
    print('That is not a valid number.')

# Note: While .isdigit() exists, it doesn't account for floats (dots) 
# or negative numbers. try/except is a more complete solution.
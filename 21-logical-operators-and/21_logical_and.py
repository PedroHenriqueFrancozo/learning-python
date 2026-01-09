"""
Topic: Logical Operators - AND
Focus: Understanding 'and' logic, Falsy values, and Short-circuit evaluation.
"""

# Logical Operators
# and (e) or (ou) not (não)
# and - All conditions must be true.
# If any value is considered false, the entire expression 
# will be evaluated as that false value.

# Falsy values: 0, 0.0, '', False
# None is used to represent "no value"

# entrance = input('[E]nter [S]exit: ')
# password_input = input('Password: ')
# authorized_password = '123456'

# if entrance == 'E' and password_input == authorized_password:
#     print('Enter')
# else:
#     print('Exit')

# Short-circuit evaluation
# It stops at the first False value and returns it
print(True and False and True)  # Returns False
print(True and 0 and True)      # Returns 0 (Falsy)
print(True and True and True)   # Returns True
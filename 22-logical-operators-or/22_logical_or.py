"""
Topic: Logical Operators - OR
Focus: Understanding 'or' logic, Truthy evaluation, and default values.
"""

# Logical Operators
# and (e) or (ou) not (não)
# or - If any condition is true, the entire expression is true.
# The expression evaluates to the first Truthy value found.

# Falsy values (already seen): 0, 0.0, '', False, None

# entrance = input('[E]nter [S]exit: ')
# password_input = input('Password: ')
# authorized_password = '123456'

# if (entrance == 'E' or entrance == 'e') and password_input == authorized_password:
#     print('Enter')
# else:
#     print('Exit')

# Short-circuit evaluation
# It stops at the first True value and returns it.
# This is commonly used to set default values:
password = input('Password: ') or 'No password provided'
print(password)

# Examples of evaluation:
print(0 or False or 'abc' or True)  # Returns 'abc'
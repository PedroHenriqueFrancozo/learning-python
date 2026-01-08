"""
Topic: VS Code Debugger and Code Execution
Focus: Watching how the Python interpreter reads each line using breakpoints.
"""

# The VS Code Debugger and the Python interpreter reading the code

condition1 = False
condition2 = False
condition3 = True
condition4 = True

if condition1:
    print('Code for condition 1')
elif condition2:
    print('Code for condition 2')
elif condition3:
    print('Code for condition 3')
elif condition4:
    print('Code for condition 4')
else:
    print('No condition was satisfied.')

if 10 == 10:
    print('Another if')

print('Outside the if')
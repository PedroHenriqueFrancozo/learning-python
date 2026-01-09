"""
Topic: While Loop with Counters
Focus: Controlling the number of repetitions using an incrementing variable.
"""

# Repetitions
# while (enquanto)
# Executes an action as long as a condition is true.
# Infinite Loop -> When the code has no end condition.

counter = 0

# The loop runs while 'counter' is less than or equal to 10
while counter < 10:
    counter = counter + 1  # Incrementing (Essential to avoid infinite loop)
    print(counter)

print('The loop has finished.')
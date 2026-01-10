"""
Topic: args - Non-named arguments
Focus: Packing and unpacking arguments within functions.
"""

# The *args operator packs all passed arguments into a tuple
def custom_sum(*args):
    total = 0
    for number in args:
        total += number
    return total

sum_result = custom_sum(1, 2, 3, 4, 5)

# Unpacking when calling the function:
numbers = (10, 20, 30, 40)
# The '*' operator spreads the tuple elements as individual arguments
total_sum = custom_sum(*numbers)

print(f'Manual sum with *args: {total_sum}')
# Built-in sum() for comparison:
print(f'Built-in sum(): {sum(numbers)}')
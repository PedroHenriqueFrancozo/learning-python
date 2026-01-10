"""
Topic: For + Range
Focus: Using the range function to generate numeric sequences.
"""

# range -> range(start, stop, step)
# start: inclusive (default is 0)
# stop: exclusive (the loop stops BEFORE this number)
# step: the increment (default is 1)

# Generates multiples of 8 from 0 to 99
numbers = range(0, 100, 8)

for number in numbers:
    print(number)
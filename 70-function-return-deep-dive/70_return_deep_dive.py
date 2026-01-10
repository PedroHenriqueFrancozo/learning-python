"""
Topic: Function return values (continued)
Focus: Capturing results and conditional returns.
"""

def add(x, y):
    # 'return' ends function execution immediately
    if x > 10:
        return [10, 20]  # Returns a list
    return x + y         # Returns the sum (int)

# Capturing return values in variables for later use
result1 = add(2, 2)
result2 = add(3, 3)

print(f'Result 1: {result1}')
print(f'Result 2: {result2}')

# Direct call with values that trigger the first 'if'
print(f'Result with x > 10: {add(11, 55)}')
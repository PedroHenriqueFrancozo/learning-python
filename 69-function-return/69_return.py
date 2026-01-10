"""
Topic: Function return values (return)
The 'return' statement terminates the function and sends a value back.
"""

def add(x, y):
    if x > 10:
        return [10, 20] # Functions can return any data type
    return x + y # Sends the result of the addition back to the caller

# Variable 'sum1' receives the value returned by the function
sum1 = add(2, 2)
sum2 = add(5, 5)
print(sum1 + sum2)

# Example returning different types
print(add(11, 0))
"""
Lesson 82: Advanced Lambda Functions
Integrating Lambdas with Higher Order Functions and Closures.
"""

def execute(function, *args):
    """Higher Order Function that runs any passed function."""
    return function(*args)

# 1. Lambda creating a Closure (Function Factory)
# m is the multiplier (captured in the closure)
# n is the number to be multiplied
double = execute(
    lambda m: lambda n: n * m,
    2
)
print(f"Closure with Lambda (2 * 2): {double(2)}")

# 2. Simple addition using Lambda
sum_result = execute(
    lambda x, y: x + y,
    2, 3
)
print(f"Simple addition (2 + 3): {sum_result}")

# 3. Lambda with *args using the sum() built-in
total_sum = execute(
    lambda *args: sum(args),
    1, 2, 3, 4, 5, 6, 7
)
print(f"Sum of multiple args (1 to 7): {total_sum}")
"""
Topic: Operator Precedence
Focus: The order in which Python executes mathematical operations.
"""

# 1. (n + n) - Parentheses have the highest priority
# 2. ** - Exponentiation
# 3. * / // % - Multiplication, Division, Integer Division, and Modulo
# 4. + - - Addition and Subtraction

# Example: (1 + 1) ** 10 -> 2 ** 10 = 1024
result_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print('Result of the expression:', result_1)
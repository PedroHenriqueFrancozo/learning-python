"""
Topic: Numeric Types (int and float)
Focus: Understanding whole numbers, floating-point numbers, ans type inspection
"""

# int -> Integer
# Represents any positive or negative whole number.
print(11)    # int
print(-11)   # int
print(0)     # int

# float -> Floating point number
# Represents any positive or negative number with a decimal point.
print(1.1, 10.11)
print(0.0, -1.5)

# The type() function shows the class of the value (type inference).
print(type('Pedro'))                   # <class 'str'>
print(type(0))                         # <class 'int'>
print(type(1.1), type(-1.1), type(0.0)) # <class 'float'>
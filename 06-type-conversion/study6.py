"""
Topic: Type Conversion (Coercion)
Focus: Converting one data type into another.
"""

# Coercion/Typecasting: converting types (str, int, float, bool)
print(int('1'), type(int('1'))) # String to Int
print(float('1') + 1)           # String to Float + Int = Float
print(bool(' '))                # Non-empty string to Boolean (True)
print(str(11) + 'b')            # Int to String (Concatenation)
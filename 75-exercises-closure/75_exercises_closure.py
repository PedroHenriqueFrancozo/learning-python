"""
Exercise: Closure and Dynamic Functions
Goal: Create functions that double, triple, and quadruple numbers
using a single base function.
"""

def make_multiplier(multiplier):
    # The inner function 'multiply' captures the 'multiplier' variable
    def multiply(number):
        return number * multiplier
    return multiply

# Creating specialized functions
double = make_multiplier(2)
triple = make_multiplier(3)
quadruple = make_multiplier(4)

# Testing results
print(f'Double 2: {double(2)}')
print(f'Triple 4: {triple(4)}')
print(f'Quadruple 5: {quadruple(5)}')
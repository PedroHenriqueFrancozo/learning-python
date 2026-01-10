"""
Sets in Python (set type)
Based on Mathematical Set Theory (Venn Diagram)
Sets are mutable, but they only accept immutable types as values.
"""

# Creating a set
# set(iterable) or {1, 2, 3}
s1 = set()  # Empty
s1 = {'Luiz', 1, 2, 3}  # With data

# Key features:
# - Do not accept mutable values (like lists);
# - Values are always unique;
# - No indexes;
# - No guaranteed order;
# - Iterable (for, in, not in).

# Example of removing duplicates
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(f'Original: {numbers} -> Set: {unique_numbers}')

# Useful methods:
s1.add('New')
s1.discard(1)
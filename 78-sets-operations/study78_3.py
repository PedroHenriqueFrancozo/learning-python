"""
Mathematical operations with sets
- Union (|): combines sets.
- Intersection (&): items present in both.
- Difference (-): items present only in the left set.
- Symmetric Difference (^): items not present in both.
"""

set_a = {1, 2, 3}
set_b = {2, 3, 4}

# 1. Union (|)
print(f'Union: {set_a | set_b}')

# 2. Intersection (&)
print(f'Intersection: {set_a & set_b}')

# 3. Difference (-)
print(f'Difference (A-B): {set_a - set_b}')

# 4. Symmetric Difference (^)
print(f'Symmetric Difference: {set_a ^ set_b}')
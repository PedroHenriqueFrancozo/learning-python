"""
Mathematical Operators in Sets (Practical Summary)
Goal: Use |, &, - and ^ operators to compare unique data collections.
"""

# Defining two sets with some common and some unique values
set_a = {1, 2, 3}
set_b = {2, 3, 4}

# Union (|): Combines everything from both sets, removing duplicates
union_result = set_a | set_b  
# Output: {1, 2, 3, 4}

# Intersection (&): Only items that exist in both sets simultaneously
intersection_result = set_a & set_b  
# Output: {2, 3}

# Difference (-): Items present ONLY in the left-side set
# Note: The order matters here!
diff_a = set_a - set_b  # Items in A that are NOT in B -> {1}
diff_b = set_b - set_a  # Items in B that are NOT in A -> {4}

# Symmetric Difference (^): Items that are unique to each set (not shared)
symmetric_result = set_a ^ set_b  
# Output: {1, 4}

# Printing results
print(f'Union: {union_result}')
print(f'Intersection: {intersection_result}')
print(f'Difference (A-B): {diff_a}')
print(f'Difference (B-A): {diff_b}')
print(f'Symmetric Difference: {symmetric_result}')
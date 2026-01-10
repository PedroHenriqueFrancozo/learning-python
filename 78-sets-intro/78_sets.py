"""
Sets in Python (set type)
Sets are mutable but only accept immutable types as values.
"""

# 1. Creating a set
s1 = set()  # Empty set
s1 = {1, 2, 3}  # Set with data

# 2. Main Characteristics
# - Unique values: they automatically remove duplicates
list_with_dupes = [1, 1, 2, 2, 3, 3]
unique_set = set(list_with_dupes)
clean_list = list(unique_set)

# - No guaranteed order and no indexes
# - They are iterable
print('Is 3 in set?', 3 in s1)

for item in s1:
    print(f'Item: {item}')
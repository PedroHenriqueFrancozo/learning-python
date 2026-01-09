"""
Topic: Iterating over strings with while
Focus: Accessing each character of a string using its index and a loop.
"""

# Indices: 012345678910
name = 'Pedro Henrique'  # Iterables have indices

index = 0
new_name = ''

# We use < (less than) because the last index is always len - 1
while index < len(name):
    letter = name[index]
    new_name += f'*{letter}'
    index += 1

new_name += '*' # Optional: adding a closing asterisk
print(new_name)
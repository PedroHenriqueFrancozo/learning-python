"""
Topic: Iterables vs Iterators
Focus: Understanding the internal mechanism of the 'for' loop using iter() and next().
"""

# Iterable -> str, range, etc. (They have the __iter__ method)
# Iterator -> The object that knows how to deliver one value at a time.
# next -> Request the next value from the iterator.
# iter -> Request the iterator from the iterable.

texto = 'Luiz'  # This is an ITERABLE

# --- WHAT THE 'FOR' LOOP DOES BEHIND THE SCENES: ---

# 1. Get the iterator from the iterable
iterator = iter(texto) 

while True:
    try:
        # 2. Keep asking for the next value
        letra = next(iterator)
        print(letra)
    except StopIteration:
        # 3. When values run out, it catches the error and stops
        break

# --- THE PYTHONIC WAY (SAME AS ABOVE): ---
print('\nUsing the for loop:')
for letra in texto:
    print(letra)
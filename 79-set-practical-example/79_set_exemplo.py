"""
Lesson 79: Practical use of Sets
Topic: Membership testing and dynamic storage.
"""

# Example of using sets to track user history
letters = set()

while True:
    letter = input('Type a letter: ')
    
    # Adding to the set (sets automatically handle duplicates)
    letters.add(letter.lower())

    # The 'in' operator is extremely efficient in sets (O(1) complexity)
    if 'l' in letters:
        print('CONGRATULATIONS! You found the hidden letter.')
        break

    print(f'Letters already typed: {letters}')
"""
Topic: Exercise - Secret Word Game
Focus: Applying while, for, enumerate, and list manipulation.
"""

# Exercise: Guess the secret word
# 1. Define a secret word
# 2. User inputs one letter at a time
# 3. Check if letter is in the word
# 4. Show revealed letters and '*' for hidden ones
# 5. Count the number of attempts

secret_word = 'Tentar'.lower()

attempts = 0
# Initialize a list of asterisks with the same length as the secret word
discovered_letters = ['*'] * len(secret_word)

while '*' in discovered_letters:
    print('\n' + ' '.join(discovered_letters))

    letter = input('Type a letter: ').lower()
    
    if len(letter) > 1:
        print('Please, type only one letter.')
        continue
        
    attempts += 1
    hit = False

    # Check each character of the secret word
    for i, secret_char in enumerate(secret_word):
        if secret_char == letter:
            discovered_letters[i] = letter
            hit = True

    if hit:
        print(f"Good guess! Letter '{letter}' found.")
    else:
        print(f"The letter '{letter}' is not in the secret word.")

# End of game
print('\n' + ' '.join(discovered_letters))
print(f'Congratulations! You found the word: "{secret_word.upper()}"')
print(f'Total attempts: {attempts}')
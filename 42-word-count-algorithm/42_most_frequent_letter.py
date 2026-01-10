"""
Topic: Algorithm - Most Frequent Letter
Focus: Using while loop and .count() to analyze string frequency.
"""

phrase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
max_frequency = 0
most_frequent_letter = ''

while i < len(phrase):
    current_letter = phrase[i]

    # Ignore spaces to focus only on characters
    if current_letter == ' ':
        i += 1
        continue

    # Count how many times the current letter appears in the whole phrase
    current_letter_count = phrase.count(current_letter)

    # Update the "champion" if the current count is higher
    if max_frequency < current_letter_count:
        max_frequency = current_letter_count
        most_frequent_letter = current_letter

    i += 1

print(
    'The letter that appeared the most was '
    f'"{most_frequent_letter}" which appeared '
    f'{max_frequency}x'
)
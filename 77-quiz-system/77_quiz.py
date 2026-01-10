"""
Exercise - Q&A System (Quiz)
Goal: Use dictionaries to create a simple quiz game.
"""

questions = [
    {
        'Question': 'How much is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    }
]

score = 0

for q in questions:
    print('Question:', q['Question'])
    print()

    options = q['Options']
    for i, opt in enumerate(options):
        print(f'{i}) {opt}')
    print()

    choice = input('Choose an option: ')
    
    is_correct = False
    if choice.isdigit():
        choice_int = int(choice)
        if 0 <= choice_int < len(options):
            if options[choice_int] == q['Answer']:
                is_correct = True

    if is_correct:
        score += 1
        print('Correct! ✅')
    else:
        print('Wrong! ❌')
    print()

print(f'You got {score} out of {len(questions)} correct.')
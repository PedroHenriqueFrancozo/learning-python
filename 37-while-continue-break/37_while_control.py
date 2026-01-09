"""
Topic: While Loop Control - Break and Continue
Focus: Skipping iterations with 'continue' and exiting with 'break'.
"""

# while (enquanto)
# Executes an action while a condition is true.
# continue -> Skips the rest of the current loop and goes back to the start.
# break -> Terminate the loop immediately.

counter = 0

while counter <= 100:
    counter += 1

    # Skipping a specific number
    if counter == 6:
        print('I will not show 6.')
        continue

    # Skipping a range of numbers
    if counter >= 10 and counter <= 27:
        print(f'Skipping the number: {counter}')
        continue

    print(counter)

    # Emergency exit
    if counter == 40:
        print('Breaking the loop at 40...')
        break

print('The loop has finished.')
"""
Topic: Logic Exercises & Robustness
Focus: Applying try/except, datetime module, and string methods (isalpha).
"""

# --- EXERCISE 1: Even or Odd ---
print("--- Exercise 1: Even or Odd ---")
try:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(f'The number {number} is EVEN.')
    else:
        print(f'The number {number} is ODD.')
except ValueError:
    print('Error: Please enter a valid INTEGER.')

# --- EXERCISE 2: Hour Greeting (Robust Version) ---
print("\n--- Exercise 2: Hour Greeting ---")
from datetime import datetime

try:
    hour_str = input("Enter the time (HH:MM): ")
    # Using datetime for professional validation
    hour_obj = datetime.strptime(hour_str, "%H:%M")
    hour = hour_obj.hour
    
    if 0 <= hour <= 11:
        print('Good morning!')
    elif 12 <= hour <= 17:
        print('Good afternoon!')
    else:
        print('Good evening!')
except ValueError:
    print("Invalid format or time. Please use HH:MM (e.g., 13:45).")

# --- EXERCISE 3: Name Length Analysis ---
print("\n--- Exercise 3: Name Length ---")
name = input('Enter your first name: ')

# .isalpha() ensures the user didn't type numbers or symbols
if name.isalpha():
    length = len(name)
    if length <= 4:
        print('Your name is short.')
    elif 5 <= length <= 6:
        print('Your name is normal.')
    else:
        print('Your name is long.')
else:
    print('Invalid input. Please use letters only (no spaces or numbers).')
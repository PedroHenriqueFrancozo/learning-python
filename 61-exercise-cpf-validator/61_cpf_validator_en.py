"""
Topic: Exercise - CPF Validator
Focus: Programming logic, data cleaning, and validation algorithms.

1. Collect the sum of the first 9 digits of the CPF 
   by multiplying each value by a countdown starting from 10.

   Example: 746.824.890-70 (First 9: 746824890)
   Weights:   10   9   8   7   6   5   4   3   2
   Digits:  x  7   4   6   8   2   4   8   9   0
   ---------------------------------------------
   Results:   70  36  48  56  12  20  32  27   0

2. Sum all the results: 
   70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

3. Multiply the total sum by 10:
   301 * 10 = 3010

4. Get the remainder of the division of the previous result by 11:
   3010 % 11 = 7

5. Verification Rule:
   If the result is greater than 9:
       The digit is 0
   Otherwise:
       The digit is the result itself.

The first digit of this CPF is 7.

Calculation of the second CPF digit:
CPF Example: 746.824.890-70

1. Collect the sum of the first 10 digits (the original 9 + the 1st calculated digit) 
   by multiplying each value by a countdown starting from 11.

   Example: 746824890 + 7
   Weights:   11  10   9   8   7   6   5   4   3   2
   Digits:  x  7   4   6   8   2   4   8   9   0   7
   -------------------------------------------------
   Results:   77  40  54  64  14  24  40  27   0  14

2. Sum all the results: 
   77 + 40 + 54 + 64 + 14 + 24 + 40 + 27 + 0 + 14 = 354

3. Multiply the total sum by 10:
   354 * 10 = 3540

4. Get the remainder of the division of the previous result by 11:
   3540 % 11 = 9

   Note: 3540 / 11 is 321 with a remainder of 9 (321 * 11 = 3531).

5. Verification Rule:
   If the result is greater than 9:
       The digit is 0
   Otherwise:
       The digit is the result itself.

The second digit of this CPF is 0 (as shown in the example 746.824.890-70).
"""
import sys

# User input
user_input_cpf = input('Enter a CPF: ')

# Data cleaning (removes dots, dashes and spaces)
clean_cpf = ''
for char in user_input_cpf:
    if char.isdigit():
        clean_cpf += char

# Check for sequential digits (e.g., 111.111.111-11)
is_sequence = clean_cpf == clean_cpf[0] * len(clean_cpf)
if is_sequence:
    print('Error: Sequential data entered.')
    sys.exit()

# Calculation of the First Digit
nine_digits = clean_cpf[:9]
countdown_1 = 10

total_result_1 = 0
for digit in nine_digits:
    total_result_1 += int(digit) * countdown_1
    countdown_1 -= 1

digit_1 = (total_result_1 * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

# Calculation of the Second Digit
ten_digits = nine_digits + str(digit_1)
countdown_2 = 11

total_result_2 = 0
for digit in ten_digits:
    total_result_2 += int(digit) * countdown_2
    countdown_2 -= 1

digit_2 = (total_result_2 * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

# Final Verification
generated_cpf = f'{nine_digits}{digit_1}{digit_2}'

if clean_cpf == generated_cpf:
    print(f'The CPF {user_input_cpf} is VALID.')
else:
    print(f'The CPF {user_input_cpf} is INVALID.')
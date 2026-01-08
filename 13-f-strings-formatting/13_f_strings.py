"""
Topic: String Formatting (f-strings)
Focus: How to format output strings with variables and decimal places.
"""

name = 'Pedro Henrique'
height = 1.80
weight = 68
imc = weight / (height * height)

# Using f-strings to format decimal places (:.2f)
# Standard: f'text {variable}'
line_1 = f'{name} has a height of {height:.2f}m'
line_2 = f'weighs {weight} kg and his BMI is {imc:.2f}'

print(line_1)
print(line_2)
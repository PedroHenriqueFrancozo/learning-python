"""
Exercise: Registration Data
Focus: Applying variables, basic math, and conditional logic.
"""

name = "Pedro"
last_name = "Francozo"
age = 20

# Calculating the birth year dynamically
current_year = 2025
birth_year = current_year - age

# Conditional to check if the person is an adult
if age >= 18:
    is_adult = "Yes"
else:
    is_adult = "No"
    
height_meters = "1.80m"

print('Name:', name)
print('Last Name:', last_name)
print('Age:', age)
print('Birth Year:', birth_year)
print('Is adult?', is_adult)
print('Height:', height_meters)
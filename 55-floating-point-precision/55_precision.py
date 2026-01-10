"""
Topic: Floating Point Imprecision
Focus: Understanding IEEE 754 and using the Decimal module for high precision.
"""
import decimal

# Standard float behavior (may show imprecision like 0.7999999999999999)
# num_1 = 0.1
# num_2 = 0.7

# Using Decimal for absolute precision
# Note: Always pass values as STRINGS to Decimal to avoid initial float bias.
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(f"Result with Decimal: {numero_3}")

# Formatting alternatives:
print(f'Formatted (f-string): {numero_3:.2f}')
print(f'Rounded (round function): {round(numero_3, 2)}')
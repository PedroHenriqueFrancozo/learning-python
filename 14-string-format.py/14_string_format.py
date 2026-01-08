"""
Topic: The .format() Method
Focus: Using named arguments and positional formatting in strings.
"""

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

# Using named arguments (nome1, nome2, nome3)
# This makes the string more readable and less dependent on variable order.
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
format_output = string.format(
    nome1=a, nome2=b, nome3=c
)

print(format_output)
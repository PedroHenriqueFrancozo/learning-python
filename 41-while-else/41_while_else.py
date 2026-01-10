"""
Topic: While / Else
Focus: Understanding the behavior of the 'else' block attached to a loop.
"""

# while/else
# The 'else' block is executed ONLY if the loop finishes naturally
# (without hitting a 'break').

string = 'Valor_qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    # This only prints if the loop goes through the entire string
    # without finding a space.
    print('Não encontrei um espaço na string.')

print('Fora do while.')
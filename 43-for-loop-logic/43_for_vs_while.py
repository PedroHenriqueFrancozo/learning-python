"""
Topic: For Loop vs While Loop
Focus: Understanding when to use each structure based on the predictability of iterations.
"""

# WHILE example (Commented out):
# Used when we DON'T know how many times the loop will run.
# It depends on a condition (password matching).
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0
# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')
#     repeticoes += 1

# FOR example:
# Used when we have an ITERABLE (like a string) and want to go through it.
texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')
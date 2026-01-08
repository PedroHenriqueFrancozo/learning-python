"""
Topic: Detailed Conditional Flow
Focus: Understanding how Python evaluates multiple conditions in a single block.
"""

# if / elif      / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

# Este é um bloco INDEPENDENTE do bloco acima
if 10 == 10:
    print('Outro if')

print('Fora do if')
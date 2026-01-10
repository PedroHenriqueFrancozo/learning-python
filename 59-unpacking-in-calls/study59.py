"""
Tópico: Desempacotamento em chamadas de funções
Focus: Spreading iterables into function arguments using the * operator.
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# O que aprendemos antes:
# a, b, c, *resto = lista

# O que aprenderemos agora: Desempacotamento em chamadas
print('Exibindo a lista crua:', lista)

print('Exibindo os itens desempacotados (*):')
print(*lista)
print(*string)
print(*tupla)

# Exemplo prático com salas (Aula 57)
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

print('\nDesempacotando matrizes:')
print(*salas, sep='\n')
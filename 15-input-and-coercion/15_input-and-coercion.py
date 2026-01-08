"""
Topic: User Input and Type Conversion
Focus: Capturing data from the terminal and converting it to numbers.
"""

# A função input() sempre retorna uma string (str).
# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Coerção (conversão de tipo) é necessária para operações matemáticas
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
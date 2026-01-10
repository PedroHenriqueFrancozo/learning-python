"""
Tópico: Operação Ternária (Condicional de uma linha)
Focus: Writing concise if/else statements for value assignment.
"""

# Estrutura: <valor> if <condicao> else <outro_valor>

condicao = 10 > 5
variavel = 'Valor se verdadeiro' if condicao else 'Valor se falso'
print(variavel)

# Exemplo prático: Verificar se um número é par ou ímpar
numero = 7
resultado = 'Par' if numero % 2 == 0 else 'Ímpar'
print(f'O número {numero} é {resultado}.')

# Exemplo com digitação de usuário
digito = 10
novo_digito = digito if digito <= 9 else 0
# Se o dígito for maior que 9, ele vira 0, senão continua sendo ele mesmo.
print(f'O dígito final é: {novo_digito}')

# Cuidado: Evite ternários aninhados (um dentro do outro), pois quebra a legibilidade.
# Exemplo de má prática:
# print('Valor' if True else 'Outro' if False else 'Fim')
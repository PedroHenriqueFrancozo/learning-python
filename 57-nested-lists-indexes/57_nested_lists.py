"""
Topic: Lists of lists (Nested Lists)
Focus: Navigating through multiple dimensions using double indices and nested loops.
"""

# Lista de listas e seus índices
salas = [
    # 0          1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# Acessando elementos específicos (Linha e depois Coluna):
# print(salas[1][0])  # Elaine
# print(salas[0][1])  # Helena
# print(salas[2][2])  # Eduarda

# Percorrendo a estrutura bidimensional:
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(f'  - {aluno}')
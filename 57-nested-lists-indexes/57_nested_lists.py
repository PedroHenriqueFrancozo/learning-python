"""
Tópico: Listas de listas (Listas Aninhadas)
Focus: Navigating through multiple dimensions using double indices and nested loops.
"""

# Lista de listas e seus índices
# List of lists and their indexes
salas = [
    # 0          1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# Acessando elementos específicos (Linha e depois Coluna):
# Accessing specific elements (Row then Column):
# print(salas[1][0])  # Elaine
# print(salas[0][1])  # Helena
# print(salas[2][2])  # Eduarda

# Percorrendo a estrutura bidimensional:
# Iterating through the 2D structure:
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(f'  - {aluno}')
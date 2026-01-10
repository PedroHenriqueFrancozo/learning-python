"""
Topic: Enumerate Function
Focus: Accessing both index and value during iteration.
"""

# enumerate - enumera iteráveis (índices)
# It creates an object that yields tuples: (index, value)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# The most common and Pythonic way to use it:
# Unpacking the tuple directly in the for loop
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# --- What happens under the hood: ---
# for item in enumerate(lista):
#     indice, nome = item  # Tuple unpacking
#     print(indice, nome)

# --- Nested Loops with Enumerate: ---
# for tupla_enumerada in enumerate(lista):
#     print('FOR of the tuple:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
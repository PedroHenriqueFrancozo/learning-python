"""
Topic: Exercise - Displaying List Indexes
Focus: Using range and len to iterate through list positions.
"""

# Exercise:
# Display the indexes and values of a list manually.
# 0 Maria
# 1 Helena
# 2 Luiz

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# range(len(lista)) generates a sequence from 0 to the last index
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
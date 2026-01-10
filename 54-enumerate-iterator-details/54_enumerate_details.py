"""
Topic: Enumerate as an Iterator
Focus: Understanding that enumerate is a lazy evaluator and gets exhausted.
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# O enumerate cria um OBJETO ITERADOR
lista_enumerada = enumerate(lista)

print('Primeiro consumo do enumerate:')
for item in lista_enumerada:
    print(item)

# Tentar usar o MESMO objeto novamente resultará em nada
print('Tentando usar o mesmo objeto novamente:')
for item in lista_enumerada:
    print(item)  # Não imprimirá nada!

# A forma correta de reuso é chamar a função diretamente no for:
print('Forma correta (sempre gera um novo iterador):')
for indice, nome in enumerate(lista):
    print(indice, nome)
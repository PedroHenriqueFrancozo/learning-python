"""
Topic: Split, Join and Strip
Focus: Cleaning and manipulating strings and lists.
"""

# split - divide uma string (gera uma list)
# join - une uma string a partir de um iterável
# strip - corta os espaços em branco do início e do fim

frase = '   Olha só que   , coisa interessante          '

# Dividindo a frase pela vírgula
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase_individual in enumerate(lista_frases_cruas):
    # .strip() remove espaços em branco extras: '  texto  ' -> 'texto'
    lista_frases.append(lista_frases_cruas[i].strip())

# Exibindo as frases limpas
print(f"Lista Limpa: {lista_frases}")

# Unindo a lista novamente em uma string, usando ', ' como separador
frases_unidas = ', '.join(lista_frases)
print(f"String Final: {frases_unidas}")
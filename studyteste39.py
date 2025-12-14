"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

i = 0
novo_nome = ''
while i <= len(nome):
    letra = (nome[i])
    novo_nome += f'*{letra}'
    i += 1
    
print(novo_nome)
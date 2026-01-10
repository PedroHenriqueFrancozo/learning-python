"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor".
"""

# 1. Criação e Acesso
pessoa = {
    'nome': 'Pedro',
    'sobrenome': 'Françozo',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
print(f"Nome: {pessoa['nome']}")

# 2. Manipulando chaves e valores
pessoa_temp = {}
chave = 'nome'
pessoa_temp[chave] = 'Pedro'
pessoa_temp['sobrenome'] = 'Françozo'
del pessoa_temp['sobrenome']

# Uso do .get() para evitar erros de KeyError
if pessoa_temp.get('sobrenome') is None:
    print('NÃO EXISTE')

# 3. Métodos úteis
pessoa.setdefault('idade', 0) # Adiciona se não existir

# 4. Shallow Copy vs Deep Copy (Cópia Rasa)
import copy
d1 = {'c1': 1, 'l1': [0, 1, 2]}
d2 = d1.copy() # l1 ainda aponta para a mesma lista na memória
d2['l1'][1] = 999999 

# 5. Update e Pop
p1 = {'nome': 'Luiz', 'sobrenome': 'Miranda'}
p1.update({'nome': 'Pedro', 'idade': 18})
print(f'Pessoa atualizada: {p1}')
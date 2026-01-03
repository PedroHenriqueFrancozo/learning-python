# Imagine um dicionário de papel: você tem uma palavra (a chave) e uma definição (o valor). No Python, funciona exatamente assim: ele armazena pares de chave: valor.

# 1. Como criar um dicionário
# Dicionários utilizam chaves {} e os pares são separados por dois pontos :.

'''
car = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
'''

# 2. Acessando e Modificando Dados
# Diferente das listas, onde você usa a posição (0, 1, 2), nos dicionários você usa a chave.

# Acessar: carro["marca"] retorna "Ford".
# Adicionar ou Atualizar: Se a chave já existir, o valor muda. Se não, ela é criada.
'''
car["cor"] = "Vermelho"
car["ano"] = 2023
'''

# Remover: Use o comando del ou o método .pop().

'''
del car["modelo"]
# ou
car.pop("ano")
'''

# Principais Métodos
# Aqui estão as funções que você mais usará no dia a dia:

'''
.keys()	Retorna todas as chaves do dicionário.
.values()	Retorna todos os valores (sem as chaves).
.items()	Retorna os pares (chave, valor) como tuplas.
.get()	Acessa um valor de forma segura (não dá erro se a chave não existir).
.clear()	Limpa todo o dicionário.
'''

# Exemplo Prático: Loop em Dicionário
# É muito comum percorrermos um dicionário para exibir as informações:

'''estudante = {'nome': 'Ana', 'curso': 'Engenharia', 'nota': 9.5}

for chave, valor in estudante.items():
    print(f'{chave.capitalize()}: {valor}')'''



# Exercício: Controle de Estoque
# Objetivo: Criar e manipular um dicionário que representa o estoque de frutas

# 1. Criação: Crie um dicionário chamado estoque com os seguintes itens:
# "Maçã": 10
# "Banana": 20
# "Laranja": 15

# 2. Atualização: Você recebeu uma nova remessa de bananas. Adicione mais 5 unidades ao valor atual da "Banana".

# 3. Adição: Um novo produto chegou! Adicione "Uva" com o valor 30 ao dicionário.

# 4. Remoção: As maçãs acabaram. Remova a chave "Maçã" do dicionário.

# 5. Exibição: Use um loop for para imprimir cada fruta e sua quantidade no formato:    
    # Produto: [nome] | Quantidade: [valor]

# 6. Cálculo: Calcule e imprima a soma total de todas as frutas no estoque.

# estoque = {
#     'Maçã': 10,
#     'Banana': 20,
# }

estoque = {
    'Maçã': {
        'quantidade': 10,
        'preço': 3.30,
    },

    'Banana': {
        'quantidade': 20,
        'preço': 3.20,
    },

    'Laranja': {
        'quantidade': 15,
        'preço': 2.50
    },

    'kiwi': {
        'quantidade': 5,
        'preço': 4.90
    }    
}

# Para chegar ao valor "lá dentro", você usa dois pares de colchetes: o primeiro para a chave externa e o segundo para a chave interna.
# Para ver os dados da Maçã: print(estoque['Maçã'])
# Para ver apenas o preço da Maçã: print(estoque['Maçã']['preco']) ou quantidade

estoque['Banana']['quantidade'] += 5
# estoque['Uva'] = 30
# estoque['Uva'] = 3.80
# Atualiza apenas o preço da Maçã, mantendo a quantidade que já existia
estoque['Maçã']['preco'] = 4.50
estoque.pop('kiwi')
estoque['Uva'] = {'quantidade': 30, 'preço': 8.90}
# print(estoque.items())

# Sistema onde o usuário cadastra o produto, você captura os dados primeiro e depois monta o dicionário:
# 1. Captura os dados
'''
nome = input("Nome da fruta: ").capitalize()
qtd = int(input("Quantidade: "))
valor = float(input("Preço: "))

# 2. Cria a nova entrada no dicionário aninhado
estoque[nome] = {
    'quantidade': qtd,
    'preco': valor
}

print(f"✅ {nome} cadastrado com sucesso!")
'''

# print('---Situação do Estoque---')
# for nome, quantidade in estoque.items():
#     print(f'Produto:{nome}: | Quantidade:{quantidade}')

# for nome, quantidade, preço in sorted(estoque.items()):
#     print(f'Produto: {nome: <10} | Quantidade: {quantidade: <5} | Preço: {preço}' )

# exibir os produtos em ordem alfabética. Para fazer isso, você pode usar a função sorted() no seu loop:
# (O : <10 serve para alinhar o texto à esquerda com 10 espaços, deixando as colunas retinhas).

# print(f'total: {sum(estoque.values())}')

print('--- Relatório de Preços ---')

# Um loop em um dicionário aninhado, a "chave" é o nome do produto, e o "valor" é o dicionário interno.
for fruta, info in estoque.items():
    # 'fruta' é a chave (ex: Maçã)
    # 'info' é o dicionário interno (ex: {'quantidade': 10, ...})
    preco = info['preço']
    qtd = info['quantidade']
    print(f'A {fruta} custa R${preco:.2f} e temos {qtd} em estoque.')

# adicionar isso ao seu código:

# 1. Peça para o usuário digitar o nome de uma fruta via input().
# 2. Use o método .get() para verificar se a fruta existe no estoque.
# 3. Se existir, imprima a quantidade. Se não, imprima "Fruta não encontrada".

print('---Bem-vindo ao Sistema de Estoque ---')
print('Degite "Sair" para encerrar')

while True:
    busca = input('Qual fruta você deseja: ').capitalize().strip() # .strip(): Usei isso no input para evitar que um espaço acidental (ex: "Uva ") estrague a busca.
    quantidade = estoque.get(busca, "Não encontrada")

    if busca == "Sair":
        print('Encerrando o sistema... Até logo!')
        break

    # if quantidade != "Não cadastrada":
    if quantidade is not None:
        print(f'Temos {quantidade} unidades de {busca} em estoque.')
    else:
        print(f'Desculpe, a fruta "{busca}" não está no sistema.')
    
    
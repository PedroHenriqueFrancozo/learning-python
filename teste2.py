# execícios de FOR

# numeros = [12, 7, 50, 3, 22, 18, 9, 6]

# for numero in numeros:
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         print(numero, 'Número impar')

# 2. Exercício: Calculadora de Investimentos

# Desenvolva um programa em Python que simule o crescimento de um investimento por 5 meses.

# Valores Iniciais:

# Crie uma variável para armazenar o saldo inicial do investimento, digamos R$ 1000,00.

# Defina uma variável para a taxa de juros mensal, digamos 1.5% (ou $0.015$).
                                                               
# Laço for: Utilize um laço for que se repita exatamente 5 vezes (uma para cada mês).

# Dica: Use range(5) ou range(1, 6) para controlar o número de repetições.

# Cálculo e Atualização: Dentro do laço, a cada repetição, você deve:

# Calcular o valor dos juros daquele mês: 
#     juros = saldo_atual * taxa.Atualizar 
# o saldo do investimento: 
#     saldo_atual = saldo_atual + juros.Exibição: 

# A cada final de mês, exiba o número do mês e o saldo total atualizado.

# saldo_atual = 1000
# taxa_juros = 0.015

# for i in range(5):
#     juros = saldo_atual * taxa_juros
#     saldo_atual = saldo_atual + juros
#     print(f' Mês {i + 1}: R$ {saldo_atual:.2f}')
#     i += 1

# 3. Exercício: Verificador de Presença (Busca em Lista)

# Desenvolva um programa que verifique se um nome específico está presente em uma lista de convidados.

# Requisitos
#  1. Lista de Convidados: Crie uma lista com alguns nomes, por exemplo:
#    convidados = ["Ana", "Bruno", "Cecília", "Daniel", "Eva", "Fábio"]

#   2. Variável Booleana: Inicialize uma variável booleana, por exemplo, encontrado, com o valor False antes de começar o laço.

#   3. Entrada do Usuário: Peça ao usuário para digitar o nome que ele deseja procurar na lista.
#       Dica: Use .capitalize() no input do usuário para garantir que a primeira letra seja maiúscula, igual aos nomes na lista (ex: "bruno" se torna "Bruno").

#   4. Laço for: Percorra a lista convidados usando o for

#   5. Verificação e Saída Rápida: Dentro do laço, verifique se o nome atual é igual ao nome buscado:
#       Se for igual, mude a variável encontrado para True.
#       Use o comando break para sair imediatamente do laço for (não precisamos continuar procurando se já encontramos!).

#   6. Resultado Final: Após o laço for terminar, use uma estrutura if/else para verificar o valor final da variável encontrado e imprimir a mensagem apropriada:
#       Se encontrado for True: Exiba "O convidado [Nome] está na lista!"
#       Se encontrado for False: Exiba "O convidado [Nome] NÃO está na lista."

# convidados = ["Ana", "Bruno", "Cecília", "Daniel", "Eva", "Fábio"]
# encontrado = False

# nome_buscado = input("Digite o nome que procura na lista: ").capitalize()

# for convidado in convidados:
#     # encontrar = convidado
#     # encontrado = True

#     if convidado == nome_buscado:
#         encontrado = True
#         break

# if encontrado:
#     print(f'O convidado {nome_buscado} está na lista.')    
# else:
#     print(f'O convidado {nome_buscado} NÃO está na lista.')

''' 
4. Exercício: Tabuada em Linha Única

Desenvolva um programa em Python que gere a tabuada de um número específico (escolhido pelo usuário) e a exiba em uma única linha, separada por espaços.

1. Entrada do Usuário: Peça ao usuário para digitar um número inteiro de 1 a 10, para o qual ele deseja a tabuada.

2. Laço for e range(): Utilize um laço for para iterar 10 vezes (para calcular a tabuada do número 1 até 10).
    Dica: Use range(1, 11).

3.Cálculo: Dentro do laço, calcule o resultado da multiplicação do número escolhido pelo usuário pelo número da iteração atual (o valor do for).

4. Impressão em Linha Única: Para fazer a impressão sem quebrar a linha, você deve usar o argumento end=' ' na função print().
    Exemplo: print(resultado, end=' ')

Exemplo de Saída
Se o usuário digitar 3, a saída deve ser:
    3 6 9 12 15 18 21 24 27 30

 O foco aqui é usar o range() corretamente e o argumento end no print() para controlar a formatação.

'''

# numero_int = input('Digite um número inteiro de 1 a 10: ')

# for i in range(1, 11):

#     multiplicacao = int(numero_int) * i

#     print(multiplicacao, end=' ')

#                            Duas soluções diferentes

# numero_str = input('Digite um número inteiro de 1 a 10: ')
# numero_int = int(numero_str)

# try:
#     if  1 <= numero_int <= 10:

#         for i in range(1, 11):
#             multiplicacao = int(numero_int) * i

#             print(multiplicacao, end=' ')
#     else:
#         print('O número deve estar entre 1 e 10.')

# except ValueError:
#     print('Entrada inválida. Por favor, digite um número inteiro.')
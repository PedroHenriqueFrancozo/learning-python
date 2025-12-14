'''
1. Exercício: Adivinhe o Número (Laços while e Módulo random)
Desenvolva um programa em Python que simule um jogo de adivinhação.

Requisitos
Gere um Número Secreto:
Você deve primeiro importar o módulo random: import random.
Gere um número inteiro aleatório entre 1 e 100 e armazene-o em uma variável: numero_secreto = random.randint(1, 100).

Variáveis de Controle:
Crie uma variável para armazenar o palpite do usuário, inicializando-a com um valor que garanta que o laço while comece (ex: palpite = 0).
Crie um contador de tentativas, inicializando-o em 0.

Laço while:
Use um laço while que continue rodando enquanto o palpite for diferente do número secreto.

Entrada e Dicas:
Dentro do while: peça ao usuário para digitar o palpite (e lembre-se de converter para int).

Aumente o contador de tentativas.

Use uma estrutura if/elif para dar dicas:
Se o palpite for maior que o secreto: Diga "Seu palpite está muito alto. Tente novamente."
Se o palpite for menor que o secreto: Diga "Seu palpite está muito baixo. Tente novamente."

Finalização:
O laço while irá parar automaticamente quando o palpite for igual ao número secreto.
Após o laço while, exiba: "Parabéns! Você acertou o número secreto ([X]) em [Y] tentativas!" (Onde X é o número secreto e Y é o contador).

'''

# import random;

# numero_secreto = random.randint(1, 100)
# palpite_int = 0
# contator_tentativas = 0

# while palpite_int != numero_secreto:
#     try:

#         palpite_jogador = input('Digite seu palpite: ')
#         palpite_int = int(palpite_jogador)

#         contator_tentativas += 1

#         if palpite_int > numero_secreto:
#             print('Seu palpite está muito alto. Tente novamente.')
#         elif palpite_int < numero_secreto:
#             print('Seu palpite está muito baixo. Tente novamente.')

#     except ValueError:
#         print('Isso não é um número válido. Tente novamente.')

# print(f'Parabéns! você acertou o número secreto {numero_secreto} em {contator_tentativas}.')

'''
2. Exercício: Validação de Senha Simples
Desenvolva um programa em Python que simule a validação de uma senha, forçando o usuário a tentar repetidamente até acertar.

Requisitos
Defina a Senha Secreta:
Defina uma variável, por exemplo, SENHA_SECRETA, com um valor fixo (ex: "12345").

Variável de Controle:
Defina uma variável de controle para o palpite do usuário, inicializando-a com um valor que garanta que o laço while comece (ex: palpite = "" ou palpite = None).

Laço while
Use um laço while que continue rodando enquanto o palpite for diferente da senha secreta.

Entrada e Repetição:
Dentro do while: Peça ao usuário para digitar a senha.
Use uma estrutura if aninhada dentro do while para dar feedback:
Se o palpite estiver errado: Exiba "Senha incorreta. Tente novamente."

Finalização:
O laço while irá parar automaticamente quando a senha digitada for igual à senha secreta.
Após o laço while, exiba: "Acesso concedido! Bem-vindo(a)."

'''

# senha = '12345'
# palpite = ''

# while palpite != senha:
#     try:
#         palpite = input('Digite a senha: ')
#         palpite_int = int(palpite)

#         if palpite_int != senha:
#             print('Senha incorreta. Tente novamente.')

#     except ValueError:
#         print('Isso não era para acontecer!')

# print('Acesso concedido! Bem-vindo(a).')
        


"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# 1. Exercício
try:
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print('O número que você digitou é par')
    else:
        print('O número que você digitou é ímpar')
except ValueError:
    print('Valor digitado não é um número inteiro válido')

# 2. Exercício
try:
    horas = int(input('Que horas são? '))
    
    if 0 <= horas <= 23:
        if horas <= 11:
            print('Bom dia!')
        elif horas >= 12 and horas <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('A hora digitada deve ser um número inteiro entre 0 e 23.')
        
except ValueError:
    print('Valor digitado não é um número inteiro válido')


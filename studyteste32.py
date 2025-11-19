"""
1. Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
2. Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
3. Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# 1. Exercício
#try:
#    numero = int(input("Digite um número inteiro: "))
#
#    if numero % 2 == 0:
#        print('O número que você digitou é par')
#    else:
#        print('O número que você digitou é ímpar')
#except ValueError:
#    print('Valor digitado não é um número inteiro válido')

# 2. Exercício
#try:
#    horario_str = input('Que horas são? (HH:MM, ex: 00:00): ')
#    partes = horario_str.split(':')
#    hora = int(partes[0])
    
#    if 0 <= hora <= 23:
#        if hora <= 11:
#            print('Bom dia!')
#        elif hora <= 17:
#            print('Boa tarde!')
#        else:
#            print('Boa noite!')
#    else:
#        print('Hora inválida')
        
#except ValueError:
#    print('Formato inválido. Use HH:MM.')
#except IndexError:
#    print('Formato inválido. Use HH:MM.')

# Outra forma do exercício 2.

#from datetime import datetime
#try:
#    horario_str = input("Digite a hora (HH:MM, ex: 13:35): ")

    # Converte a string para um objeto de data/hora, usando o formato "%H:%M"
#    objeto_hora = datetime.strptime(horario_str, "%H:%M")
    
    # Agora você extrai o componente de hora validado
#    hora = objeto_hora.hour
    
    # A sua lógica de saudação continua aqui, usando a variável 'hora'
#    if hora <= 11:
#        print('Bom dia!')
#    elif hora <= 17:
#        print('Boa tarde!')
#    else:
#        print('Boa noite!')
        
#except ValueError:
    # Este erro é disparado se a string não estiver no formato %H:%M ou se os valores forem inválidos (ex: 25:00)
#    print("Formato inválido ou hora/minuto fora do intervalo (use HH:MM).")

# 3. Exercício

#nome = input('Digite seu nome: ')
    
#if len(nome) <= 4:
#        print('Seu nome é muito curto.')
#elif len(nome) <= 6:
#    print('Seu nome é normal.')
#else:
#    print('Seu nome é grande.')

# Resolvendo de forma mais robusta a quetão

#nome = input('Digite seu nome: ')

#if nome.isalpha():

#    tamanho = len(nome)

#    if len(nome) <= 4:
#        print('Seu nome é muito curto.')
#    elif len(nome) <= 6:
#        print('Seu nome é normal.')
#    else:
#        print('Seu nome é grande.')

#else:
#    print('Entrada inválida. Por favor, digite apenas letras.')


'''
O que aprendi

    1. Estrutura de Tratamento de erro

Para lidar com a possibilidade de o usuário digitar algo que não é um número inteiro(como "abc" ou "3.5"), usar o bloco try...except .
    O código que lida com o erro fica dentro do except.

    O bloco try...except é ideal para lidar com erros de tipo ou erros de execução esperados (como ValueError, IndexError, etc.), Por exemplo:
        Tentar converter texto para número(int('abc'))
        tentar dividir por zero.
    O input usado para obter uma dados do usuário nunca vai disparar um erro se o usuário digitar "Pedro123" ou "123". Ele simplesmente armezena o texto.


Como lidar com data e hora no Python. Vídeo sobre o assunto (https://www.youtube.com/watch?v=eBYSjP4vf_w)

    Uma opção simples para separar horas e munutos é usar o .split()

outra opção Robusta usar o Módulo datatime
    
    Para códigos mais comploxos ou que precisam de precisão, a melhor prática é usar a biblioteca nativa do python chamada datetime.
    Ela lida com a validação do formato, horas, minutos e até fusos horários de forma automática.

    usar o método strptime (string parse time) para transformar a string do usuário em ("13:35") em um objeto de hora real.

3. Estrutura usada no terceiro execício

    O método .isalpha()
    Ele retorna True se todos os caracteres na string forem letras (a-z, A-Z).
    Ele retorna False se a string contiver qualquer número, espaço, pontuação ou caractere especial.
    
'''
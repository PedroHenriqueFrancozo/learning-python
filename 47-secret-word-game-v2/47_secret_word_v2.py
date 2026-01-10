"""
Topic: Exercise - Secret Word Game (Version 2)
Focus: String manipulation, accumulation, and terminal clearing with 'os'.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # 1. Verification Logic
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # 2. Display Logic
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    # 3. Winning Condition
    if palavra_formada == palavra_secreta:
        os.system('clear')  # Limpa o terminal (use 'cls' se estiver no Windows)
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        
        # Reset para uma nova rodada ou sair
        letras_acertadas = ''
        numero_tentativas = 0
        break
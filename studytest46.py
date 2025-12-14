"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavras_secreta = 'Tentar'.lower()

tentativas = 0
letras_descobertas = ['*'] * len(palavras_secreta)

while '*' in letras_descobertas:

    print('\n' + ' '.join(letras_descobertas))

    letra = input('Digite uma letra: ').lower()
    tentativas += 1

    acertou = False

    for i, char_secreto in enumerate(palavras_secreta):

        if char_secreto == letra:
            letras_descobertas[i] = letra
            acertou = True

    if acertou:
        print(f"Bom palpite! Letra '{letra}' encontrada.")
    else:
        print('Não encontramos a letra na palavra secreta.')

print(' '.join(letras_descobertas))
print(f'Você encontrou todas as letra da palavra {palavras_secreta}, tentativas {tentativas}')

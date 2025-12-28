"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

while True:

    cpf_usuario = input('Digite apenas os números do seu CPF: ')
    cpf_limpo = cpf_usuario.replace('.', '').replace('-', '').replace(' ', '')

    if not cpf_limpo.isdigit():
        print('Erro: O CPF deve conter apenas número.')
        continue

    if len(cpf_limpo) != 11:
        print('Erro: O CPF deve conter 11 dígitos.')
        continue

    nove_digitos = cpf_limpo[:9]
    contardor_regressivo_um = 10
    soma_primeiro_digito = 0

    for digito_um in nove_digitos:
        soma_primeiro_digito += int(digito_um) * contardor_regressivo_um
        contardor_regressivo_um -= 1
    digito_um = (soma_primeiro_digito * 10) % 11

    digito_um = digito_um if digito_um <= 9 else 0

    print(f'Resultado do primeiro digito é:  {digito_um}')


    dez_digitos = cpf_limpo[:10]
    soma_segundo_digito = 0
    contardor_regressivo_dois = 11

    for digito_dois in dez_digitos:
        soma_segundo_digito += int(digito_dois) * contardor_regressivo_dois
        contardor_regressivo_dois -= 1
#        print(soma_segundo_digito)
    digito_dois = (soma_segundo_digito % 11)

    if int(digito_dois) >= 2:
        digito_dois = 11 - digito_dois
    else:
        digito_dois = 0

    print(f'Resultado do segundo digito é:  {digito_dois}')

    novo_cpf = f'{nove_digitos}{digito_um}{digito_dois}'
    
    if cpf_usuario == novo_cpf:
        print(f'{novo_cpf} Verdadeiro')
    else:
        print(f'{novo_cpf} Falso')

    break



    
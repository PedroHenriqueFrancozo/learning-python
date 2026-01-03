# Exercício: Simulador de Sistema de RH (Salário Líquido)

# O Problema:
# O RH precisa calcular o salário final de um funcionário após os descontos.
# O salário bruto é calculado por: horas_trabalhadas * valor_hora.
# Há um desconto fixo de imposto de 10%.
# Há um bônus de R$ 50,00 se o funcionário trabalhou mais de 160 horas no mês.


# funcionario = 'Pedro'
# horas_trabalhadas = 160
# valor_hora = 8
# desconto = 10
# valor_bonus = 50

# def salario_bruto(horas_trabalhadas, valor_hora):
#     salario = horas_trabalhadas * valor_hora
#     print(f'Salario = {salario}')
#     return salario

# def desconto_fixo(desconto, salario_bruto):
#     calculo_desconto = (salario_bruto * desconto) / 100
#     print(f'Desconto = {calculo_desconto}')
#     calculo_desconto = salario_bruto - calculo_desconto
#     print(f'dd {calculo_desconto}')
#     return calculo_desconto # salário R$1152

# def bonus(horas_trabalhadas, desconto_fixo, valor_bonus):
#     if horas_trabalhadas >= 160:
#         print(f'Você recebeu R${valor_bonus} no seu salário')
#         valor_bonus = desconto_fixo + valor_bonus
#         print(f'R${valor_bonus} seu salário')
#     else:
#         print(f'Você não obteve o resultado para receber bônus')
#     return valor_bonus #salário R$1202

# def salario_final(bonus):
#     print(f'Funcionário {funcionario} seu salário final é de R${bonus}')
#     return salario_final

# salario_bruto = salario_bruto(horas_trabalhadas, valor_hora)
# desconto_fixo = (desconto_fixo(desconto, salario_bruto))
# bonus = bonus(horas_trabalhadas, desconto_fixo, valor_bonus)
# salario_final = salario_final(bonus)


# Refatorando o código


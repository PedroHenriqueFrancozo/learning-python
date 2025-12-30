# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplication(*args):
    total = 1
    for number in args:
            total *= number
    return total

result = multiplication(1, 2, 3, 4, 5)
print(result)
# print(1 * 2 * 3 * 4 * 5)

# Crie uma função fala se um número é par ou impar.
# Retorne se o número é par ou ímpar
 
def pair_odd(number):
    multiplo = number % 2 == 0 
    
    if multiplo:
        return f'O número {number} é par'
    return f'O número {number} é ímpar'

print(pair_odd(10))

    

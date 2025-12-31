# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicate(number):
#     return number * 2

# def triple(number):
#     return number * 3

# def quadruple(number):
#     return number * 4

# result = duplicate(10)
# result_triple = triple(result)
# result_quadruple = quadruple(result_triple)

# print(result_quadruple)

def criar_multiplicador(multiplicador):
    def multiplicar(number):
        return number * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)


print(duplicar(2))
print(triplicar(4))
print(quadruplicar(5))
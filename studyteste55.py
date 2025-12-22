"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""

lista_de_compras = []
opcao_cliente = ""

while True:
    print("Seleciona uma opção")
    opcao_cliente = input("[i]nserir [a]pagar [l]istar: ")
    
    if opcao_cliente == "i":
        valor_inserido = input("Valor: ")
        lista_de_compras.append(valor_inserido)
        print(f'"{valor_inserido}" foi adcionado com sucesso!')

    try:
        if opcao_cliente == "a":
            apagar = input("Qual item deseja apagar: ")
            lista_de_compras.removea(apagar)
            print(f'"{apagar}" item removido com sucesso!')
        
        elif opcao_cliente == "l":
            print(lista_de_compras)

    except ValueError:
        print("Por favor, digite um valor correspondente.")
    except:
        print("Esse índice não existe na lista.")




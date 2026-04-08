from b import *
from time import sleep as t
opcoes = ["add", "listar", "pesquisar", "buscar", "editar", "remover", "sair"]
def menu():
    print("-="*20)
    for x, opcao in enumerate(opcoes):
        print(f"{x + 1}° Opção >>> {opcao}")
    print("-="*20)
def algo1():
    print("Você escolheu opcao 1")
def algo2():
    print("Você escolheu opcao 2")
def algo3():
    print("Você escolheu opcao 3")
def algo4():
    print("Você escolheu opcao 4")
def algo5():
    print("Você escolheu opcao 5")
def algo6():
    print("Você escolheu opcao 6")
def sair():
    print("Saindo", end = "", flush = True)
    for x in range(3):
        print(".", end = "", flush = True)
        t(0.5)
    print("\nFim")
def main():
    opcao = "Loop"
    funcoes = [menu, 1, 2, 3, 4, 5, 6, sair]
    while opcao != "Parada":
        conexcao = criarConexao("localhost", "Usuario", "Senha", "Banco de dados")
        inicializarTabela(conexcao)
        menu()
        opcao = int_input("Opcao: ", True)
        for pos, funcao in enumerate(funcoes):
            if opcao == pos:
                funcao()
                if opcao == 7:
                    opcao = "Parada"
                    encerrarConexao(conexcao)

main()



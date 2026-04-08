import mysql.connector
from time import sleep as t

def criar_conexao():
    conexao = mysql.connector.connect(host = "localhost", user = "root", password = "1234")
    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS db;")
    cursor.execute("USE DATABASE db;")
    cursor.execute("CREATE TABLE IF NOT EXISTS ouvidoria (ID INT AUTO_INCREMENT PRIMARY KEY, reclamacao VARCHAR(900) NOT NULL);")
    cursor.close()
    return conexao

def menu():
    opcoes = ["Adicionar", "Listar", "Pesquisar", "Editar", "Quantidade","Remoção", "Sair"]
    for pos, opcao in enumerate(opcoes):
        print(f"{pos+1}° Opção: {"->":^10} {opcao} ")

def int_input(msg, verificacao = False):
    tentativa = input(msg).strip()
    while tentativa.isnumeric() == False or (verificacao == True and tentativa not in "1234567"):
        tentativa = input("Tente novamente: ").strip()
    return int(tentativa)

def add(conexao, cursor):
    reclamacao = input("Digite sua reclamação").strip()
    while len(reclamacao) == 0:
        reclamacao = input("Digite uma reclamação que não esteja vazia: ").strip()
    cursor.execute("INSERT INTO ouvidoria(reclamacao) VALUES (%s);", (reclamacao,))
    cursor.commit()
    cursor.close()

def listar(conexao, cursor, vazio = False, qntia = False):
    cursor.execute("SELECT * FROM ouvidoria;")
    lista = cursor.fetchall()
    if qntia == True:
        return (len(lista)
    if len(lista) = 0:
        print("A lista está vazia")
        t(1.5)
        return True
    else:
        if vazio == False:
            for pos, reclamacao in enumerate(lista):
                print(f"ID: {pos + 1}  | Reclamação: {reclamacao}")
                t(0.5)
            t(1)
        return False
    
def vazio(conexao, cursor):
    verificacao = listar(conexao, cursor, vazio = True)
    return verificacao
    
    
def buscar(conexao, cursor, resultado = False):
    if not vazio(conexao, cursor):
        try:
            cursor.execute ("SELECT * FROM ouvidoria WHERE id = (%s);", (int_input("ID: ",))
            id = cursor.fetchall()[0]
            if resultado == True:
                return id
        except:
            print("Esse ID está indisponível no momento, tente novamente")
def editar(conexao,cursor)
    id = buscar(conexao, cursor, resultado = True)

def qnt(conexao, cursor):
    tamanho = busca(conexao, cursor, qntia = True)
    print(f"Há {tamanho} reclamações no momento")

def remover(conexao, cursor):
    id = (conexao, cursor, resultado = True)
    cursor.execute (f"DELETE * from ouvidoria WHERE id = {%s};", (id,))
    
    
def sair(conexao, cursor):
    print("Saindo", flush = True, end = "")
    for x in range(3):
        t(0.5)
        print(".", flush = True, end = "")
    cursor.close()
    conexao.close()

def main():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    opcao = "Loop"
    funcoes = [menu, add, listar, pesquisar, editar, qnt, remover, sair]
    while opcao != "Parada":
        menu()
        opcao = int_input("Número da opção: ", verificacao = True)
        for x, funcao in enumerate(funcoes):
            if opcao == x:
                funcao(conexao, cursor)
                if x == 7:
                    opcao = "Parada"
main()

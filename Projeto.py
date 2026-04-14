'''Projeto 2026.1 Fase 2 (Ouvidoria + MYSQL)
Trabalho feito por João Henrique de França e Silva e Joel Nicollas Silva Pereira
Última edição: 14/04/2026 9:04
'''

import mysql.connector
from time import sleep as t

def criar_conexao():
    conexao = mysql.connector.connect(host = "localhost", user = "root", password = "admin") #Ou qualquer outra senha
    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS banco_dados;")
    cursor.execute("USE banco_dados;")
    cursor.execute("CREATE TABLE IF NOT EXISTS reclamacoes(id INT AUTO_INCREMENT PRIMARY KEY, reclamacao VARCHAR(900));")
    cursor.close()
    return conexao

def vazio(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM reclamacoes;")
    tamanho = cursor.fetchone()[0]
    if tamanho == 0:
        print("A lista está vazia")
        t(1.5)
        cursor.close()
        return True
    else:
        return False

def menu():
    opcoes = ["Adicionar", "Listar", "Pesquisar", "Editar", "Quantidade","Remoção", "Sair"]
    for pos, opcao in enumerate(opcoes):
        print(f"{pos+1}° Opção: {'->':^10} {opcao} ")

def int_input(msg, verificacao = False):
    tentativa = input(msg).strip()
    while tentativa.isnumeric() == False or (verificacao == True and tentativa not in "1234567"):
        tentativa = input("Tente novamente: ").strip()
    return int(tentativa)

def add(conexao):
    cursor = conexao.cursor()
    reclamacao = input("Digite sua reclamação: ").strip()
    cursor.execute("INSERT INTO reclamacoes(reclamacao) VALUES (%s);", (reclamacao,))
    conexao.commit()
    cursor.close()
    print("Reclamação adicionada!")
    t(1.5)

def listar(conexao):
    if not vazio(conexao):
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM reclamacoes;")
        lista = cursor.fetchall()
        for reclamacao in lista:
            item = {"ID": reclamacao[0], "Reclamação": reclamacao[1]}
            print(f"ID: {item['ID']}  | Reclamação: {item['Reclamação']}")
            t(0.5)
        cursor.close()
        t(1)
    
def pesquisar(conexao, busca = False):
    if not vazio(conexao):
        try:
            cursor = conexao.cursor()
            cursor.execute ("SELECT * FROM reclamacoes WHERE id = (%s);", (int_input("ID: "),))
            resultado_query = cursor.fetchall()[0]
            item = {"ID": resultado_query[0], "Reclamação": resultado_query[1]}
            print(f"ID: {item["ID"]}  | Reclamação: {item["Reclamação"]}")
            t(1.5)
            if busca == True:
                cursor.close()
                return item["ID"]
        except:
            print("Esse ID está indisponível no momento, tente novamente.")
            t(1.5)
            cursor.close()
            return None
    
def editar(conexao):
    if not vazio(conexao):
        cursor = conexao.cursor()
        id = pesquisar(conexao, busca = True)
        if id is not None:
            reclamacao = input("Digite sua reclamação: ").strip()
            cursor.execute("UPDATE reclamacoes SET reclamacao = (%s) WHERE id = (%s);", (reclamacao, id))
            conexao.commit()
            print("Reclamação editada!")
            t(1.5)
        cursor.close()

def qnt(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM reclamacoes;")
    tamanho = cursor.fetchone()[0]
    print(f"Há {tamanho} reclamações no momento.")
    cursor.close()
    t(1.5)

def remover(conexao):
    if not vazio(conexao):
        cursor = conexao.cursor()
        id = pesquisar(conexao, busca = True)
        if id is not None:
            cursor.execute ("DELETE FROM reclamacoes WHERE id = (%s);", (id,))
            conexao.commit()
            print("Reclamação excluída!")
            t(1.5)
        cursor.close()

def sair(conexao):
    print("Saindo", flush = True, end = "")
    for x in range(3):
        t(0.5)
        print(".", flush = True, end = "")
    conexao.close()

def main():
    conexao = criar_conexao()
    opcao = "Loop"
    funcoes = [add, listar, pesquisar, editar, qnt, remover, sair]
    while opcao != "Parada":
        menu()
        opcao = int_input("Número da opção: ", verificacao = True)
        funcao = funcoes[opcao - 1]
        funcao(conexao)
        if opcao == 7:
            opcao = "Parada"
main()

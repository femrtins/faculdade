# Autoras: Monique Ellen dos Santos e Fernanda Ribeiro Martins
# Data: 6 de dezembro de 2023

# Esse script se conecta a um banco de dados MySQL chamado "teste" e cadastra users

# Observações:
# A execução do script depende da existência prévia do banco de dados "teste" e da tabela "livro".
# Certifique-se de ter a biblioteca `mysql-connector-python` instalada (`pip install mysql-connector-python`).

import mysql.connector
import os



mydb = mysql.connector.connect(
    # Estabelece uma conexão com o banco de dados MySQL, utilizando as credenciais fornecidas (
    # host, usuário, senha) e selecionando o banco de dados 'teste'.

    host="localhost",
    user= "root",
    password="Iamon1402",
    database="teste"
)

mycursor = mydb.cursor()    # Cria um cursor para interagir com o banco de dados.

def getUsers():
    """
    Função que recupera e imprime todos os usuários cadastrados 
    no banco de dados.
    """

    print ("\n=========== Usuario cadastrados =================\n")

    mycursor.execute("SELECT User FROM mysql.user where Host='%';")
    users =mycursor.fetchall()

    for user in users:
        print(user[0])


def verificarUser(usuario):
    """
    Verifica se um usuário já está cadastrado no banco de dados.
    Retorna True se o usuário já existe, False caso contrário.
    :param usuario: String com o nome do user
    """

    mycursor.execute("SELECT User FROM mysql.user where Host='%';")
    users =mycursor.fetchall()

    for user in users:
        if usuario==user[0]:
            return True
    
    return False


def cadastro(mod):
    """
    Cadastra um novo usuário no banco de dados. Retorna True se o 
    cadastro for bem-sucedido, False caso contrário.
    :param mod: Tipo de usuário (1 para Administrador, 2 para Consulta).    
    """

    usuario = input("Digite o nome do novo usuario: ")

    if verificarUser(usuario):
        print("Usuario já cadastrado!")
        return False
    
    senha = input("Digite a senha: ")

    mycursor.execute("CREATE USER %s@'%' IDENTIFIED BY %s;", (usuario, senha))
    
    mycursor.execute("GRANT EXECUTE ON PROCEDURE teste.login_trigger TO %s@'%';", (usuario,))
    mycursor.execute("GRANT UPDATE, SELECT, INSERT ON teste.controle_de_acesso TO %s@'%';", (usuario,))
    mycursor.execute("FLUSH PRIVILEGES;")

    if mod==1:

        mycursor.execute("GRANT UPDATE, INSERT, DELETE, SELECT ON teste.livro TO %s@'%';", (usuario,))
        mycursor.execute("GRANT INSERT, SELECT ON teste.livro_log TO %s@'%';", (usuario,))

    else:

        mycursor.execute("GRANT SELECT ON teste.livro TO %s@'%';", (usuario,))

    return True

def relatorio():
    """
    Exibe um relatório de todos os usuários cadastrados no 
    banco de dados.
    """

    os.system("clear")

    print ("\n===========Cadastrar novo usuario=================\n")

    print ("1. Administrador")
    print ("2. Consulta")
    task= int(input("Insira uma opcao: "))
    os.system("clear")
    
    if(task==1):
        op = cadastro(1)
    elif(task==2):
        op =cadastro(2)
    else:
        op = False
        print ("Voce informou um número invalido\n")

    if op:
        os.system("clear")
        getUsers()

        mydb.commit()
        mydb.close()
    
    print ("\n==================================================")


# Chamada da função para exibir o relatório
relatorio()

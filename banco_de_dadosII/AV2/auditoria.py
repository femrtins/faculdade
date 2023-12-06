# Autoras: Monique Ellen dos Santos e Fernanda Ribeiro Martins
# Data: 6 de dezembro de 2023

# Esse script se conecta a um banco de dados MySQL chamado "teste" e realiza uma operação de
# leitura na tabela "controle_de_acesso".

# Observações:
# A execução do script depende da existência prévia do banco de dados "teste" e da tabela "livro".
# Certifique-se de ter a biblioteca `mysql-connector-python` instalada (`pip install mysql-connector-python`).

import mysql.connector


mydb = mysql.connector.connect(    
    # Estabelece uma conexão com o banco de dados MySQL, utilizando as credenciais fornecidas (
    # host, usuário, senha) e selecionando o banco de dados 'teste'.

    host="localhost",
    user= "root",
    password="Iamon1402",
    database="teste"
)

mycursor = mydb.cursor()     # Cria um cursor para interagir com o banco de dados.

def relatorio():
    """
    Gerar um relatório com todos os dados da tabela 
    'controle_de_acesso'. Imprime os resultados no 
    terminal.
    """

    print ("===========Todos os dados da tabela=================\n")

    mycursor.execute("select * from controle_de_acesso")   # Cursor executa o comando select *

    rows = mycursor.fetchall()                             # As linhas são salvas na váriavel rows

    for row in rows:
        print("ID_CONEXAO:", row[1], ", USER:", row[2], ", LOGIN_TS:", row[3], 
        ", LOGOUT_TS:", row[4], ", QTD_SELECT:", row[5], ", QTD_INSERT:", row[6], 
        ", QTD_DELETE:", row[7], ", QTD_UPDATE:", row[8])
        print("")

    print ("\n====================================================")

def main():
    """
    Função principal que chama a função relatorio() 
    para exibir os dados da tabela. Realiza o commit 
    e fecha a conexão com o banco de dados ao final.
    """

    relatorio()
    mydb.commit()
    mydb.close()
    
main()

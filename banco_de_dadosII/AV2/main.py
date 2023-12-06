# Autoras: Monique Ellen dos Santos e Fernanda Ribeiro Martins
# Data: 6 de dezembro de 2023

# Este script interage com um banco de dados MySQL chamado "teste", realizando operações de inserção,
# seleção, exclusão e atualização de registros na tabela "livro". O script também inclui funcionalidades
# de controle de acesso, como logoff e verificação de privilégios de usuário.

# Observações:
# A execução do script depende da existência prévia do banco de dados "teste" e da tabela "livro".
# Certifique-se de ter a biblioteca `mysql-connector-python` instalada (`pip install mysql-connector-python`).


import mysql.connector
import os

os.system("clear")
usuario = input("Digite o nome de usuário do banco de dados: ")
senha = input("Digite a senha do banco de dados: ")


mydb = mysql.connector.connect(
    # Estabelece uma conexão com o banco de dados MySQL, utilizando as credenciais fornecidas (
    # host, usuário, senha, banco de dados) e selecionando o banco de dados 'teste'.

    host="localhost",                     
    user= usuario,                       
    password= senha,                      
    database= "teste"                 
)

mycursor = mydb.cursor()    # Cria um cursor para interagir com o banco de dados.

def grants():
    """
    Verifica os privilégios do usuário no banco de dados.
    Retorna 1 se o usuário tiver privilégios de administrador, 
    2 se for apenas de consulta.
    """

    mycursor.execute("SHOW GRANTS FOR %s@'%';", (usuario,))
    resultado = mycursor.fetchall()
    print(len(resultado))
    if len(resultado)>4:
        return 1
    return 2
    

def logoff():
    """
    Atualiza os registros de acesso ao banco de dados 
    ao fazer logoff.
    """

    mycursor.execute("SHOW STATUS LIKE 'Com_select';")
    select = mycursor.fetchall()

    mycursor.execute("SHOW STATUS LIKE 'Com_delete';")
    delete = mycursor.fetchall()

    mycursor.execute("SHOW STATUS LIKE 'Com_update';")
    update = mycursor.fetchall()

    info = (select[0][1], delete[0][1], update[0][1] )
    sql = "update controle_de_acesso set logout_ts = NOW(), qtd_select = %s, qtd_delete = %s, qtd_update = %s WHERE id_conexao = CONNECTION_ID();"
    mycursor.execute(sql, info)
    mydb.commit()
                     
def fim():
    """
    Função para pausar a execução até que o usuário 
    pressione Enter
    """
    input("Pressione Enter para continuar...")
    os.system("clear")


def inserir():
    '''
    Função que insere livros na tabela fornecidos 
    pelo usuário.
    '''

    isbn= str(input("Digite o codigo ISBN: "))
    nome= str(input("Digite o nome da obra:"))
    autor= str(input("Digite o nome do autor:"))
    genero= str(input("Digite o genero:"))

    mycursor.execute("insert into livro values (%s, %s, %s, %s)",(isbn, nome, autor, genero))
    mydb.commit()

    
    print("\n============= Livro adicionado ==============\n")# Imprimir verificação
    selecionar(isbn)

def selecionar(isbn = None):
    """
    Imprime os dados da tabela de livros.
    Se o parâmetro ISBN for fornecido, imprime 
    apenas o livro correspondente.
    :param isbn: String com o Padrão Internacional 
    de Numeração de Livro.
    """

    if isbn != None:
        sql = "SELECT * FROM livro WHERE isbn = %s"
        mycursor.execute(sql, (isbn,))
    else:
        mycursor.execute("select * from livro")

    rows = mycursor.fetchall()
    for row in rows:
        print("ISBN:", row[0], ", Título:", row[1], ", Autor:", row[2], ", Genero:", row[3])
    print ("\n==============================================")

def getLivro(isbn):
    """
    Retorna informações de um livro com base no ISBN.
    Função para usuários somente com grant de consulta.
    :param isbn: String com o Padrão Internacional 
    de Numeração de Livro.
    """

    sql = "SELECT * FROM livro WHERE isbn = %s"
    mycursor.execute(sql, (isbn,))

    result=mycursor.fetchall()
    
    return result[0]


def deletar():
    """
    Deleta um livro da tabela de livros.
    """

    print ("===========Todos os dados da tabela=================\n")
    selecionar()

    del_isbn= input("Insira isbn do livro a deletar: ")
    sql = "delete from livro where isbn = %s"

    mycursor.execute(sql, (del_isbn,))
    mydb.commit()

    os.system("clear")
    
    print ("========= Livro excluido =====================\n")  # Livro excluido da tabela de log
    sql = "SELECT * FROM livro_log WHERE isbn = %s order by timestamp_column DESC limit 1"
    mycursor.execute(sql, (del_isbn,))

    rows = mycursor.fetchall()
    for row in rows:
        print("ISBN:", row[0], ", Título:", row[1], ", Autor:", row[2], ", Genero:", row[3])
    print ("\n==============================================")


def atualizacao():
    """
    Realiza a atualização de informações de um livro na tabela.
    """

    print ("===========Todos os dados da tabela=================\n")
    selecionar()

    print("(Informe os dados ou enter para continuar)\n")

    
    isbn = input("Informe o isbn do livro para update: ")   # Isbn do livro para update

    livro = getLivro(isbn)                                  # Livro antes das mudanças

    lista = ["", "", "", ""]                                # Mudanças livro
    lista[0] = isbn
    lista[1] = input("Informe o nome: ")
    lista[2] = input("Informe o autor: ")
    lista[3] = input("Informe o genero: ")


    for i in range(len(livro)):
        if lista[i] == "":
            lista[i] = livro[i]

    update = "UPDATE livro SET nome=%s, autor=%s, genero=%s WHERE isbn=%s" 
    mycursor.execute(update, (lista[1], lista[2], lista[3], lista[0]))
    mydb.commit()

    os.system("clear")

    
    print ("========= Versao antiga =====================\n")# Imprimir versao antiga

    sql = "SELECT * FROM livro_log WHERE isbn = %s order by timestamp_column DESC limit 1"
    mycursor.execute(sql, (lista[0],))

    rows = mycursor.fetchall()

    for row in rows:
        print("ISBN:", row[0], ", Título:", row[1], ", Autor:", row[2], ", Genero:", row[3])

    

    print ("\n========= Versao atual =====================\n") # Imprimir versao nova
    selecionar(lista[0])


def administrador():
    """
    Função para as ações do administrador.
    """

    while(True):
        print ("==============================================")
        print ("0. Fim")
        print ("1. Inserir")
        print ("2. Selecionar")
        print ("3. Deletar")
        print ("4. Fazer atualização")
        print ("==============================================")
        task= int(input("Insira uma opcao: "))
        os.system("clear")
        
        if(task==1):
            inserir()
        elif(task==2):
            print ("===========Todos os dados da tabela=================\n")
            selecionar()
        elif(task==3):
            deletar()
        elif(task==4):
           atualizacao()
        elif(task==0):
            break
        else:
            print ("Voce informou um número invalido\n")
        fim()

    mydb.commit()

    logoff()
    mydb.close()
    print ("Fim do programa!\n")

def consulta():
    """
    Função para as ações do user com permisão só de consulta.
    """

    while(True):
        print ("==============================================")
        print ("0. Fim")
        print ("1. Selecionar")
        print ("==============================================")
        task= int(input("Insira uma opcao: "))
        os.system("clear")
        
        if(task==1):
            selecionar()
        elif(task==0):
            break
        else:
            print ("Voce informou um número invalido\n")
        fim()

    mydb.commit()

    logoff()
    mydb.close()
    print ("Fim do programa!\n")

def main():
    """
    Função principal que chama a função administrador() 
    ou consulta() dependendo das permissões do user.
    """

    if grants()==1:
        administrador()
    
    else:
        consulta()

if __name__ == '__main__':
    main()

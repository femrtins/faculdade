# Autoras: Monique Ellen dos Santos e Fernanda Ribeiro Martins
# Data: 6 de dezembro de 2023

# Este script Python tem como objetivo realizar a inserção de informações sobre livros em um banco de dados MySQL 
# chamado 'teste'. Utiliza o módulo mysql.connector para se conectar ao banco de dados e efetuar as inserções 
# na tabela 'livro'.

# Observações:
# A execução do script depende da existência prévia do banco de dados "teste" e da tabela "livro".
# Certifique-se de ter a biblioteca `mysql-connector-python` instalada (`pip install mysql-connector-python`).

import mysql.connector                 



mybd = mysql.connector.connect(
    # Estabelece uma conexão com o banco de dados MySQL, utilizando as credenciais fornecidas (
    # host, usuário, senha) e selecionando o banco de dados 'teste'.

    host = 'localhost',
    user ='root',
    password ='Iamon1402',
    database ='teste'
)

mycursor = mybd.cursor() # Cria um cursor para interagir com o banco de dados.

def adicionar_livro(isbn, nome, autor, genero):
    """
    A função recebe quatro valores de string e 
    adiona-as como um registro no banco de dados.
    :param isbn: String do Padrão Internacional 
    de Numeração de Livro (char (13))
    :param nome: String do titulo do livro
    :param autor: String com o nome do autor
    :param genero: String com o gênero do livro   
    """

    query = "INSERT INTO livro (isbn, nome, autor, genero) VALUES (%s, %s, %s, %s)"
    values = (isbn, nome, autor, genero)

    try:
        mycursor.execute(query, values)
        mybd.commit()
        print('Livro adicionado com sucesso!')

    except mysql.connector.Error as err:
        print(f"Erro ao adicionar livro: {err}")

def fim():
    """
    Função para fechar o cursor e a conexão com 
    o banco de dados.
    """
    mycursor.close()
    mybd.close()

def main():
    """
    Função principal que adiciona uma lista de 
    livros ao bd.
    """

    adicionar_livro('9780137135266', 'Clean Code', 'Robert C. Martin', 'Programação')
    adicionar_livro('9780316416896', 'The Martian', 'Andy Weir', 'Ficção Científica')
    adicionar_livro('9780451457998', 'Neuromancer', 'William Gibson', 'Ficção Científica')
    adicionar_livro('9780061120084', 'To Kill a Mockingbird', 'Harper Lee', 'Romance')
    adicionar_livro('9781400034772', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Ficção')
    adicionar_livro('9780140283334', '1984', 'George Orwell', 'Ficção Científica')
    adicionar_livro('9780060850524', 'The Catcher in the Rye', 'J.D. Salinger', 'Romance')
    adicionar_livro('9780316769486', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'História')
    adicionar_livro('9780735224629', 'Educated', 'Tara Westover', 'Biografia')
    adicionar_livro('9780062457738', 'The Subtle Art of Not Giving a F*ck', 'Mark Manson', 'Autoajuda')
    adicionar_livro('9780670026196', 'All the Light We Cannot See', 'Anthony Doerr', 'Ficção Histórica')
    adicionar_livro('9780143110632', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('9780316015844', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('9780143110342', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9781400064281', 'The Goldfinch', 'Donna Tartt', 'Ficção')
    adicionar_livro('9780307277679', 'The Kite Runner', 'Khaled Hosseini', 'Ficção Histórica')
    adicionar_livro('9780385504201', 'A Game of Thrones', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('9780061122415', 'The Alchemist', 'Paulo Coelho', 'Ficção')
    adicionar_livro('9780671027346', 'Angels & Demons', 'Dan Brown', 'Suspense')
    adicionar_livro('9780553382563', 'The Shack', 'William P. Young', 'Religião')
    adicionar_livro('9780143038412', 'The Da Vinci Code', 'Dan Brown', 'Mistério')
    adicionar_livro('9780345538376', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9780525951054', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('9780307454546', 'Water for Elephants', 'Sara Gruen', 'Romance')
    adicionar_livro('9780060548785', 'Life of Pi', 'Yann Martel', 'Aventura')
    adicionar_livro('9780812998603', 'The Underground Railroad', 'Colson Whitehead', 'Ficção Histórica')
    adicionar_livro('9780743273565', 'The Catcher in the Rye', 'J.D. Salinger', 'Romance')
    adicionar_livro('9780385311390', 'Jurassic Park', 'Michael Crichton', 'Ficção Científica')
    adicionar_livro('9780307887436', 'The Night Circus', 'Erin Morgenstern', 'Fantasia')
    adicionar_livro('9780451526342', 'Brave New World', 'Aldous Huxley', 'Ficção Científica')
    adicionar_livro('9780316330318', 'Ready Player One', 'Ernest Cline', 'Ficção Científica')
    adicionar_livro('9780316015844', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('9780451191144', 'One Hundred Years of Solitude', 'Gabriel García Márquez', 'Realismo Mágico')
    adicionar_livro('9780544003287', 'The Hobbit', 'J.R.R. Tolkien', 'Fantasia')
    adicionar_livro('9780062316097', 'The Fault in Our Stars', 'John Green', 'Romance')
    adicionar_livro('9780061950728', 'The Hunger Games', 'Suzanne Collins', 'Ficção Científica')
    adicionar_livro('9780141189574', 'One Flew Over the Cuckoo\'s Nest', 'Ken Kesey', 'Ficção')

    adicionar_livro('9780316769486', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'História')
    adicionar_livro('9780735224629', 'Educated', 'Tara Westover', 'Biografia')
    adicionar_livro('9780062457738', 'The Subtle Art of Not Giving a F*ck', 'Mark Manson', 'Autoajuda')
    adicionar_livro('9780670026196', 'All the Light We Cannot See', 'Anthony Doerr', 'Ficção Histórica')
    adicionar_livro('9780143110632', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('9780316015844', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('9780143110342', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9781400064281', 'The Goldfinch', 'Donna Tartt', 'Ficção')
    adicionar_livro('9780307277679', 'The Kite Runner', 'Khaled Hosseini', 'Ficção Histórica')
    adicionar_livro('9780385504201', 'A Game of Thrones', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('9780061122415', 'The Alchemist', 'Paulo Coelho', 'Ficção')
    adicionar_livro('9780671027346', 'Angels & Demons', 'Dan Brown', 'Suspense')
    adicionar_livro('9780553382563', 'The Shack', 'William P. Young', 'Religião')
    adicionar_livro('9780143038412', 'The Da Vinci Code', 'Dan Brown', 'Mistério')
    adicionar_livro('9780345538376', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9780525951054', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('9780307454546', 'Water for Elephants', 'Sara Gruen', 'Romance')
    adicionar_livro('9780060548785', 'Life of Pi', 'Yann Martel', 'Aventura')
    adicionar_livro('9780812998603', 'The Underground Railroad', 'Colson Whitehead', 'Ficção Histórica')
    adicionar_livro('9780743273565', 'The Catcher in the Rye', 'J.D. Salinger', 'Romance')
    adicionar_livro('9780385311390', 'Jurassic Park', 'Michael Crichton', 'Ficção Científica')
    adicionar_livro('9780307887436', 'The Night Circus', 'Erin Morgenstern', 'Fantasia')
    adicionar_livro('9780451526342', 'Brave New World', 'Aldous Huxley', 'Ficção Científica')
    adicionar_livro('9780316330318', 'Ready Player One', 'Ernest Cline', 'Ficção Científica')
    adicionar_livro('9780316015844', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('9780451191144', 'One Hundred Years of Solitude', 'Gabriel García Márquez', 'Realismo Mágico')
    adicionar_livro('9780544003287', 'The Hobbit', 'J.R.R. Tolkien', 'Fantasia')
    adicionar_livro('9780062316097', 'The Fault in Our Stars', 'John Green', 'Romance')
    adicionar_livro('9780061950728', 'The Hunger Games', 'Suzanne Collins', 'Ficção Científica')
    adicionar_livro('9780141189574', 'One Flew Over the Cuckoo\'s Nest', 'Ken Kesey', 'Ficção')

    adicionar_livro('9780307474278', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9781400067947', 'The Secret Life of Bees', 'Sue Monk Kidd', 'Drama')
    adicionar_livro('9780142000663', 'The Lovely Bones', 'Alice Sebold', 'Drama')
    adicionar_livro('9780679745587', 'Midnight in the Garden of Good and Evil', 'John Berendt', 'Não Ficção')
    adicionar_livro('9780451524935', 'East of Eden', 'John Steinbeck', 'Drama')
    adicionar_livro('9780441013593', 'The Name of the Wind', 'Patrick Rothfuss', 'Fantasia')
    adicionar_livro('9780316769486', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'História')
    adicionar_livro('9781400034772', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Ficção')
    adicionar_livro('9780812988406', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('9780060935467', 'Memoirs of a Geisha', 'Arthur Golden', 'Romance Histórico')
    adicionar_livro('9780062315007', 'Gone Girl', 'Gillian Flynn', 'Suspense')
    adicionar_livro('9780316491329', 'Where the Crawdads Sing', 'Delia Owens', 'Mistério')
    adicionar_livro('9780307346627', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('9780441172719', 'The Stand', 'Stephen King', 'Ficção Pós-Apocalíptica')
    adicionar_livro('9780385514231', 'A Clash of Kings', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('9780345539878', 'The Goldfinch', 'Donna Tartt', 'Ficção')
    adicionar_livro('9781400069590', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9780316015844', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('9780143110342', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9780062255655', 'The Silent Wife', 'A.S.A. Harrison', 'Suspense')
    adicionar_livro('9780451203592', 'The Red Tent', 'Anita Diamant', 'Ficção Histórica')
    adicionar_livro('9780375727344', 'The Devil in the White City', 'Erik Larson', 'História')
    adicionar_livro('9780385315541', 'The Five People You Meet in Heaven', 'Mitch Albom', 'Ficção')
    adicionar_livro('9780451169532', 'Jurassic Park', 'Michael Crichton', 'Ficção Científica')
    adicionar_livro('9781400033416', 'The Da Vinci Code', 'Dan Brown', 'Mistério')
    adicionar_livro('9780553384772', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('9780452284246', 'The Glass Castle', 'Jeanette Walls', 'Biografia')
    adicionar_livro('9780307592736', 'A Dance with Dragons', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('9780452286868', 'Freakonomics', 'Steven D. Levitt', 'Economia')
    adicionar_livro('9780812988406', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('9781400067947', 'The Secret Life of Bees', 'Sue Monk Kidd', 'Drama')
    adicionar_livro('9780142000663', 'The Lovely Bones', 'Alice Sebold', 'Drama')
    adicionar_livro('9780679745587', 'Midnight in the Garden of Good and Evil', 'John Berendt', 'Não Ficção')
    adicionar_livro('9780451524935', 'East of Eden', 'John Steinbeck', 'Drama')
    adicionar_livro('9780441013593', 'The Name of the Wind', 'Patrick Rothfuss', 'Fantasia')
    adicionar_livro('9780316769486', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'História')
    adicionar_livro('9781400034772', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Ficção')
    adicionar_livro('9780812988406', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('9780060935467', 'Memoirs of a Geisha', 'Arthur Golden', 'Romance Histórico')
    adicionar_livro('9780062315007', 'Gone Girl', 'Gillian Flynn', 'Suspense')
    adicionar_livro('9780316491329', 'Where the Crawdads Sing', 'Delia Owens', 'Mistério')
    adicionar_livro('9780307346627', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('9780441172719', 'The Stand', 'Stephen King', 'Ficção Pós-Apocalíptica')
    adicionar_livro('9780385514231', 'A Clash of Kings', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('9780345539878', 'The Goldfinch', 'Donna Tartt', 'Ficção')
    adicionar_livro('9781400069590', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9780316015844', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('9780143110342', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('9780062255655', 'The Silent Wife', 'A.S.A. Harrison', 'Suspense')

    adicionar_livro('4120556016951', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('4150664086539', 'The Secret Life of Bees', 'Sue Monk Kidd', 'Drama')
    adicionar_livro('4160813085726', 'The Lovely Bones', 'Alice Sebold', 'Drama')
    adicionar_livro('4170718079189', 'Midnight in the Garden of Good and Evil', 'John Berendt', 'Não Ficção')
    adicionar_livro('4180816035020', 'East of Eden', 'John Steinbeck', 'Drama')
    adicionar_livro('4190441015375', 'The Name of the Wind', 'Patrick Rothfuss', 'Fantasia')
    adicionar_livro('4200786926740', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'História')
    adicionar_livro('4210674165071', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Ficção')
    adicionar_livro('4221101475179', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('4230385495509', 'Memoirs of a Geisha', 'Arthur Golden', 'Romance Histórico')
    adicionar_livro('4240385538685', 'Gone Girl', 'Gillian Flynn', 'Suspense')
    adicionar_livro('4250525559731', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('4260441172711', 'The Stand', 'Stephen King', 'Ficção Pós-Apocalíptica')
    adicionar_livro('4270385514239', 'A Clash of Kings', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('4280345539875', 'The Goldfinch', 'Donna Tartt', 'Ficção')
    adicionar_livro('4291400069598', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('4300316015846', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('4310143110342', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('4320062255657', 'The Silent Wife', 'A.S.A. Harrison', 'Suspense')
    adicionar_livro('4330451203594', 'The Red Tent', 'Anita Diamant', 'Ficção Histórica')
    adicionar_livro('4340375727342', 'The Devil in the White City', 'Erik Larson', 'História')
    adicionar_livro('4350385315546', 'The Five People You Meet in Heaven', 'Mitch Albom', 'Ficção')
    adicionar_livro('4360451169533', 'Jurassic Park', 'Michael Crichton', 'Ficção Científica')
    adicionar_livro('4371400033419', 'The Da Vinci Code', 'Dan Brown', 'Mistério')
    adicionar_livro('4380553384775', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('4390452284249', 'The Glass Castle', 'Jeanette Walls', 'Biografia')
    adicionar_livro('4400307592739', 'A Dance with Dragons', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('4410452286869', 'Freakonomics', 'Steven D. Levitt', 'Economia')
    adicionar_livro('4420812988407', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('4431400067949', 'The Secret Life of Bees', 'Sue Monk Kidd', 'Drama')
    adicionar_livro('4440142000664', 'The Lovely Bones', 'Alice Sebold', 'Drama')
    adicionar_livro('4450679745589', 'Midnight in the Garden of Good and Evil', 'John Berendt', 'Não Ficção')
    adicionar_livro('4460451524936', 'East of Eden', 'John Steinbeck', 'Drama')
    adicionar_livro('4470441013594', 'The Name of the Wind', 'Patrick Rothfuss', 'Fantasia')
    adicionar_livro('4480316769487', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'História')
    adicionar_livro('4491400034773', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Ficção')
    adicionar_livro('4500812988408', 'The Girl on the Train', 'Paula Hawkins', 'Suspense')
    adicionar_livro('4510060935468', 'Memoirs of a Geisha', 'Arthur Golden', 'Romance Histórico')
    adicionar_livro('4520062315008', 'Gone Girl', 'Gillian Flynn', 'Suspense')
    adicionar_livro('4530316491329', 'Where the Crawdads Sing', 'Delia Owens', 'Mistério')
    adicionar_livro('4540307346628', 'The Road', 'Cormac McCarthy', 'Ficção Pós-Apocalíptica')
    adicionar_livro('4550441172712', 'The Stand', 'Stephen King', 'Ficção Pós-Apocalíptica')
    adicionar_livro('4560385514232', 'A Clash of Kings', 'George R.R. Martin', 'Fantasia')
    adicionar_livro('4570345539879', 'The Goldfinch', 'Donna Tartt', 'Ficção')
    adicionar_livro('4581400069591', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('4590316015845', 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Mistério')
    adicionar_livro('4600143110343', 'The Help', 'Kathryn Stockett', 'Drama')
    adicionar_livro('4610062255656', 'The Silent Wife', 'A.S.A. Harrison', 'Suspense')

    fim()

main()

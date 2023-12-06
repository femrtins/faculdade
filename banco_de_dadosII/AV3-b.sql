AV3-b

Esta avaliação ocorrerá sobre a base de dados Sakila, portanto dedique um tempo para compreender essa base de dados.

AÇÕES A SEREM FEITAS:

A1) elaborar e fornecer comandos SQL que utilizem os recursos abaixo. Além do comando SQL, você deve fornecer também uma descrição textual explicando no que consistem os resultados retornados. Caso queira, pode também explicar o SQL.

a) consultas aninhadas

----- SELECIONAR OS TITULOS DOS FILMES QUE A ATRIZ PENELOPE GUINESS ATUOU

SELECT title FROM film
WHERE film.film_id in ( SELECT film_id FROM film_actor
                    WHERE actor_id in (SELECT actor_id FROM actor
                                      WHERE first_name like "PENELOPE" AND last_name like "GUINESS")
                  );

b) consultas aninhadas correlacionadas

----- SELECIONAR OS ATORES CUJA PRIMEIRA LETRA DO NOME NÃO PERTENCE 
A PRIMEIRA LETRA DO NOME DE NENHUM PAÍS

SELECT *
FROM actor 
WHERE NOT EXISTS
      (SELECT country from country
      WHERE LEFT(country,1) = LEFT(first_name,1)
);
      
c) exists 

----- SELECIONAR ATORES QUE TEM NOMES IGUAIS A NOMES DE CLIENTES

SELECT * FROM actor
WHERE EXISTS 
   (SELECT first_name, last_name FROM customer
    WHERE first_name=actor.first_name AND last_name=actor.last_name
);

d) unique ou distinct

----- TABELA TEMPORÁRIA COM OS 10 FILMES MAIS ALUGADOS
CREATE TEMPORARY TABLE filmes_mais_alugados
AS SELECT inventory.film_id
  FROM rental JOIN inventory on rental.inventory_id=inventory.inventory_id
  GROUP BY inventory.film_id
  ORDER BY COUNT(*) DESC LIMIT 10;

----- NOMES ORDENADOS DOS ATORES QUE ESTAVAM NOS 10 FILMES MAIS ALUGADOS

SELECT DISTINCT actor.first_name, actor.last_name
FROM actor, film_actor
WHERE actor.actor_id = film_actor.actor_id AND
      film_actor.film_id in (SELECT * from filmes_mais_alugados) ORDER BY first_name ASC;


e) junções naturais

----- SELECIONAR TODOS OS ATORES DE LADY STAGE

SELECT film_actor.film_id,  film.title, 
       film_actor.actor_id, actor.first_name, actor.last_name
from (actor join film_actor on actor.actor_id=film_actor.actor_id) join film on film.film_id=film_actor.film_id 
WHERE film.title like "LADY STAGE";

f) junção left ou right

----- QUANTIDADE DE FILMES QUE NÃO TEM NA LOJA 2

SELECT COUNT(DISTINCT film.film_id)
FROM film LEFT JOIN inventory on inventory.film_id = film.film_id AND inventory.store_id=2
WHERE inventory.store_id IS NULL;


g) agregação

------ SELECIONAR O NUMERO DE PAGAMENTOS E O VALOR MEDIO PAGO PELOS CLIENTES NA LOJA 1

SELECT COUNT(amount), AVG(amount)
FROM payment, staff
WHERE payment.staff_id=staff.staff_id AND staff.store_id=1;

h) group by

------ EXIBIR OS FILMES DE MAIOR DURAÇÃO DE CADA CATEGORIA

SELECT category.name, film.title, film.length
FROM (category JOIN film_category on category.category_id=film_category.category_id) 
      JOIN film on film.film_id=film_category.film_id 
WHERE (category.name, film.length) in 
      (SELECT category.name, MAX(film.length)
      FROM (category JOIN film_category on category.category_id=film_category.category_id) 
            JOIN film on film.film_id=film_category.film_id
      GROUP BY category.name);

A2) fornecer o comando de criação de uma visão;

------ VIEW COM A QUANTIDADE DE CLIENTES DE CADA PAÍS DO MUNDO

CREATE VIEW cliente_por_pais
AS SELECT country.country, COUNT(*) as num_clientes
FROM (customer JOIN address on customer.address_id = address.address_id)
      JOIN city on address.city_id=city.city_id 
      JOIN country on country.country_id=city.country_id
GROUP BY country.country_id;

A3) elaborar um programa (sugestão: em python) que percorra os registros obtidos por um dos comandos SQL's que foi criado nos itens "a" a "h".
-------------------------------------------------------
#Percorrer registros obtidos pelo comando SQL do item e

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iamon_14",
    database="sakila"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT film_actor.film_id,  film.title, \
       film_actor.actor_id, actor.first_name, actor.last_name \
from (actor join film_actor on actor.actor_id=film_actor.actor_id) join film on film.film_id=film_actor.film_id  \
WHERE film.title like 'LADY STAGE'")

myresult = mycursor.fetchall()

print("ATORES DE LADY STAGE: \n")
for x in myresult:
    print("- ", x[3], x[4])
-------------------------------------------------------

PARA TODAS AS RESPOSTAS FORNEÇA TAMBÉM um ou mais print's da tela, demonstrando a execução do comando.

O envio ocorrerá por meio de um link de acesso aos arquivos (endereço de repositório, google drive, etc). Sugere-se o uso de repositórios para compor portfólio pessoal de aprendizagem.

FIM

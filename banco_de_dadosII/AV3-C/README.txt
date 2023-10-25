CREATE TABLE livro(
	isbn char(13) NOT NULL PRIMARY KEY,
	nome varchar(255) NOT NULL,
	autor varchar(255) NOT NULL,
	genero varchar(255)	
)

create table livro_log(
	isbn char(13) NOT NULL,
	nome varchar(255) NOT NULL,
	autor varchar(255) NOT NULL,
	genero varchar(255)	
)

drop table livro_log;
select * from livro;

use meubd

insert into livro values("9788595084759", "A sociedade do anel", "J. R. R. Tolkien", "Terror");
INSERT  into livro values("9788535930344", "As intermitências da morte", "José Saramago", "Romance Português");

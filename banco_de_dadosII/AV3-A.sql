Avaliação AV3

Aluno(a)s: -- Monique Ellen dos Santos
	   -- Fernanda Ribeiro Martins

a) apresente o valor x encontrado

x = 1.358883662511648

b) apresente o(s) SQL(s) utilizado(s) para encontrar x

-- DESCOBRIR O X:

SELECT 
	(SELECT AVG("Annual Salary" / 252 ) from main_table WHERE "Salary or Hourly" = "Salary") /
	(SELECT AVG(("Hourly Rate") * "Typical Hours"/5) from main_table WHERE "Salary or Hourly" ="Hourly");


c) apresente o comando update

begin;

UPDATE main_table 
SET "Hourly Rate" = "Hourly Rate" * 
(SELECT 
	(SELECT AVG("Annual Salary" / 252 ) from main_table WHERE "Salary or Hourly" = "Salary") /
	(SELECT AVG(("Hourly Rate") * "Typical Hours"/5) from main_table WHERE "Salary or Hourly" ="Hourly"))
WHERE "Salary or Hourly" = "Hourly";

commit;

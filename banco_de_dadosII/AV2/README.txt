
# Estratégias para controle de acesso ao banco de dados (auditoria) 


Por meio da auditoria temos uma fonte que permite gerar relatórios/rastrear ações do usuário no banco de dados.


De que forma podemos armazenar as principais informações referentes a manipulação e consulta de dados de um usuário durante uma sessão mysql? 



## Estratégias
Por meio de procedimentos armazenados e triggers

Por meio de um programa python

## Procedimento armazenado e Triggers

Problema: Não foi encontrada uma forma de acionar um procedimento de logoff_trigger após encerrar uma conexão.

Problema: Não é possível atualizar para fins de auditoria a quantidade de select e o timestamp de logout do usuário.
## </Resultados> Procedures e Triggers

SELECT id, id_conexao, user, login_ts, qtd_insert
FROM controle_de_acesso;

| id | id_conexao | user              | login_ts            | qtd_insert |
|----|------------|-------------------|---------------------|------------|
| 1  | 25         | fe@localhost      | 2023-12-03 19:40:20 | 0          |
| 2  | 31         | fe@localhost      | 2023-12-03 20:43:46 | 1          |
| 3  | 32         | fe@localhost      | 2023-12-03 20:52:22 | 2          |
| 4  | 29         | fe@localhost      | 2023-12-05 09:56:16 | 1          |
| 5  | 31         | fe@localhost      | 2023-12-05 09:56:38 | 4          |
| 6  | 33         | monique@localhost | 2023-12-05 10:58:48 | 0          |



SELECT user, COUNT(user) AS count 
FROM controle_de_acesso 
GROUP BY user 
ORDER BY count DESC;

| user              | login_ts            |
|-------------------|---------------------|
| fe@localhost      | 5                   |
| monique@localhost | 1                   |



## </Resultados> Programa Python

ID_CONEXAO: 68 , USER: fernanda@localhost , LOGIN_TS: 2023-12-04 12:47:52 , 
LOGOUT_TS: 2023-12-04 12:47:54 , 
QTD_SELECT: 1 , QTD_INSERT: 0 , QTD_DELETE: 0 , QTD_UPDATE: 0

ID_CONEXAO: 84 , USER: monique@localhost , LOGIN_TS: 2023-12-04 13:09:43 , 
LOGOUT_TS: 2023-12-04 13:09:48 , 
QTD_SELECT: 1 , QTD_INSERT: 0 , QTD_DELETE: 0 , QTD_UPDATE: 0

ID_CONEXAO: 43 , USER: root@localhost , 
LOGIN_TS: 2023-12-05 10:07:45 , 
LOGOUT_TS: None , 
QTD_SELECT: 0 , QTD_INSERT: 1 , QTD_DELETE: 1 , QTD_UPDATE: 1

Problema: Só é possível realizar consultas genéricas usando select

No programa python os dados são obtidos a partir dos status da sessão após o usuário optar por finalizar as consultas/atualizações: 

SHOW STATUS LIKE 'Com_select';
## Considerações finais
Uma estratégia mais adequada dependerá do objetivo pretendido com a auditoria. 
O programa em python pode ser complementado para de adequar as necessidades de um projeto específico. Enquanto  triggers/procedures possuem a limitação da ausência de de quantidade de select e timestamp final.


##Referências
https://fromdual.com/mysql-logon-and-logoff-trigger-for-auditing
https://fromdual.com/sites/default/files/logon_trigger_wp.pdf

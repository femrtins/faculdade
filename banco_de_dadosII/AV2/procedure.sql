DELIMITER $

CREATE PROCEDURE teste.login_trigger()
SQL SECURITY DEFINER
BEGIN
  INSERT INTO controle_de_acesso (id_conexao, user, login_ts)
  VALUES (CONNECTION_ID(), USER(), NOW());
END;

$
DELIMITER ;

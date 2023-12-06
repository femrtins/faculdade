DELIMITER $

CREATE TRIGGER after_insert_trigger
AFTER INSERT ON livro
FOR EACH ROW
BEGIN

  UPDATE controle_de_acesso
     SET qtd_select = qtd_select+1
   WHERE id_conexao = CONNECTION_ID();
END;

$
DELIMITER ;

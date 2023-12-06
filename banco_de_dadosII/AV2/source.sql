DELIMITER $

    -- Criar Trigger para atualizar row na tabela
    CREATE TRIGGER atualizar_no_log BEFORE UPDATE ON livro FOR EACH ROW
    BEGIN       
        -- adiciona o registro antigo ao log
        INSERT INTO livro_log VALUES(OLD.isbn, OLD.nome, OLD.autor, OLD.genero, NOW());
    END$


    -- Trigger para excluir row da tabela
    CREATE TRIGGER excluir_no_log BEFORE DELETE ON livro FOR EACH ROW
    BEGIN       
        -- adiciona o registro antigo ao log
        INSERT INTO livro_log VALUES(OLD.isbn, OLD.nome, OLD.autor, OLD.genero, NOW());
    END$

DELIMITER ;

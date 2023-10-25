DELIMITER $
    -- Criar Trigger para inserir row no log antes de inserir uma nova linha na tabela
    
    CREATE TRIGGER inserir_no_log BEFORE INSERT ON livro FOR EACH ROW
    BEGIN       
        -- obtem o isbn do livro que vai ser inserido
        SET @old_isbn = (SELECT isbn from livro where isbn = NEW.isbn);
        -- verifica se o isbn já exite
        IF @old_isbn = NEW.isbn THEN
            INSERT INTO livro_log VALUES(NEW.isbn, NEW.nome, NEW.autor, NEW.genero);
            -- DELETE FROM livro WHERE isbn = NEW.isbn;
        END IF;
    END$

DELIMITER ;

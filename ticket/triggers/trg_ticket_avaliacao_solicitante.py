def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_avaliacao_solicitante()
        RETURNS TRIGGER AS $$
            DECLARE _empresa_id integer;

            BEGIN
                IF (OLD.avaliacao_solicitante = 0 AND NEW.avaliacao_solicitante > 0) THEN
                    _empresa_id := SELECT empresa_id FROM usuario WHERE id = NEW.atendente_id;

                    UPDATE
                        usuario 
                    SET 
                        media_avaliacoes = fnc_media_avaliacao_atendente(NEW.atendente_id)
                    WHERE
                        id = NEW.atendente_id;
                    
                    UPDATE
                        empresa
                    SET
                        media_avaliacoes = fnc_media_avaliacao_empresa(_empresa_id)
                    WHERE
                        id = _empresa_id;
                END IF;
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_avaliacao_solicitante ON ticket;
        CREATE TRIGGER trg_ticket_avaliacao_solicitante
        AFTER UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_avaliacao_solicitante();
    """

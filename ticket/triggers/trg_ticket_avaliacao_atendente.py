def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_avaliacao_atendente()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (OLD.avaliacao_solicitante IS NULL AND NEW.avaliacao_solicitante IS NOT NULL) THEN
                    UPDATE usuario SET media_avaliacoes = fnc_media_avaliacao_usuario(NEW.atendente_id, true) WHERE id = NEW.atendente_id;
                END IF;
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_avaliacao_atendente ON ticket;
        CREATE TRIGGER trg_ticket_avaliacao_atendente
        AFTER UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_avaliacao_atendente();
    """

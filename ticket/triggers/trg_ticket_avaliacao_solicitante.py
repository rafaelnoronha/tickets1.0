def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_avaliacao_solicitante()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (OLD.avaliacao_solicitante IS NULL AND NEW.avaliacao_solicitante IS NOT NULL) THEN
                    UPDATE usuario SET media_avaliacoes = fnc_media_avaliacao_atendente(NEW.atendente_id) WHERE id = NEW.atendente_id;
                END IF;
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_avaliacao_solicitante ON ticket;
        CREATE TRIGGER trg_ticket_avaliacao_solicitante
        AFTER UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_avaliacao_solicitante();
    """

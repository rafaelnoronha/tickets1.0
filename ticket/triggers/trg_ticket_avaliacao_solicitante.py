def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_avaliacao_solicitante()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (OLD.avaliacao_atendente IS NULL AND NEW.avaliacao_atendente IS NOT NULL) THEN
                    UPDATE usuario SET media_avaliacoes = fnc_media_avaliacao_usuario(NEW.solicitante_id, true) WHERE id = NEW.solicitante_id;
                END IF;
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_avaliacao_solicitante ON ticket;
        CREATE TRIGGER trg_ticket_avaliacao_solicitante
        AFTER UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_avaliacao_solicitante();
    """
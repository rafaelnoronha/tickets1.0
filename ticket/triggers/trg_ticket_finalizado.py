def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_finalizado()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (OLD.finalizado_id IS NULL AND NEW.finalizado_id) THEN
                    NEW.data_finalizacao := NOW();
                    NEW.hora_finalizacao := NOW();
                END IF;
                    
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_finalizado ON ticket;
        CREATE TRIGGER trg_ticket_finalizado
        BEFORE UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_finalizado();
    """

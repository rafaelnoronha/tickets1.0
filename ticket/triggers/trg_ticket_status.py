def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_status()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (NULLIF(NEW.cancelado_id, 0) > 0) THEN NEW.status := '4';
                ELSEIF (NULLIF(NEW.finalizado_id, 0) > 0) THEN NEW.status := '3';
                ELSEIF (NULLIF(NEW.solucionado_id, 0) > 0) THEN NEW.status := '2';
                ELSEIF (NULLIF(NEW.atendente_id, 0) > 0) THEN NEW.status := '1';
                ELSE NEW.status := '0';
                END IF;
                
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_status ON ticket;
        CREATE TRIGGER trg_ticket_status
        BEFORE INSERT OR UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_status();
    """

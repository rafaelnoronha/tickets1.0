def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_cancelado()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (OLD.cancelado_id IS NULL AND NEW.cancelado_id IS NOT NULL) THEN
                    NEW.data_cancelamento := NOW();
                    NEW.hora_cancelamento := NOW();
                END IF;
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_cancelado ON ticket;
        CREATE TRIGGER trg_ticket_cancelado
        BEFORE UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_cancelado();
    """
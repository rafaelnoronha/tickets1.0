def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_status()
        RETURNS TRIGGER AS $$
            DECLARE _status varchar;

            BEGIN
                IF (NULLIF(NEW.cancelado_id, 0) > 0) THEN _status := '4';
                ELSEIF (NULLIF(NEW.finalizado_id, 0) > 0) THEN _status := '3';
                ELSEIF (NULLIF(NEW.solucionado_id, 0) > 0) THEN _status := '2';
                ELSEIF (NULLIF(NEW.atendente_id, 0) > 0) THEN _status := '1';
                ELSE _status := '0';
                END IF;
                
                UPDATE ticket SET status = _status WHERE id = NEW.ticket_id;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_status ON ticket;
        CREATE TRIGGER trg_ticket_status
        AFTER INSERT ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_status();
    """

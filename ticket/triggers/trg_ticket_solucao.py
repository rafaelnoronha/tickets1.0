def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_solucao()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (NEW.solucionado_id IS NOT NULL) THEN
                    IF (OLD.solucionado_id IS NULL OR OLD.solucionado_id <> NEW.solucionado_id) THEN
                        NEW.data_solucao := NOW();
                        NEW.hora_solucao := NOW();
                    END IF;
                ELSE
                    NEW.data_solucao := null;
                    NEW.hora_solucao := null;
                END IF;
            
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_solucao ON ticket;
        CREATE TRIGGER trg_ticket_solucao
        BEFORE UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_solucao();
    """

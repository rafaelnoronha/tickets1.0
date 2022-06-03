def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_atendente()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (TG_OP = 'UPDATE') THEN
                    IF (OLD.atendente_id IS NULL AND NEW.atendente_id IS NOT NULL) THEN
                        NEW.data_atribuicao_atendente := NOW();
                        NEW.hora_atribuicao_atendente := NOW();
                    END IF;
                ELSEIF (TG_OP = 'INSERT') THEN
                    IF (NEW.atendente_id IS NOT NULL) THEN
                        NEW.data_atribuicao_atendente := NOW();
                        NEW.hora_atribuicao_atendente := NOW();
                    END IF;
                END IF;
                
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_atendente ON ticket;
        CREATE TRIGGER trg_ticket_atendente
        BEFORE INSERT OR UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_atendente();
    """

def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_mensagem_ticket_solucao()
        RETURNS TRIGGER AS $$
            DECLARE ultimo_movimento record;

            BEGIN
                IF (NEW.solucao) THEN
                    SELECT * INTO ultimo_movimento FROM movimento_ticket WHERE ticket_id = NEW.ticket_id ORDER BY ticket_id DESC LIMIT 1;

                    INSERT INTO movimento_ticket(ticket_id, solucao_id) VALUES(NEW.ticket_id, NEW.id);
                END IF;
                
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_mensagem_ticket_solucao ON mensagem_ticket;
        CREATE TRIGGER trg_mensagem_ticket_solucao
        AFTER INSERT ON mensagem_ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_mensagem_ticket_solucao();
    """

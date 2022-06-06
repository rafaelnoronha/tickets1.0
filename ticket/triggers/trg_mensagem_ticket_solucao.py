def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_mensagem_ticket_solucao()
        RETURNS TRIGGER AS $$
            BEGIN
                IF (NEW.solucao) THEN
                    UPDATE ticket SET solucionado_id = NEW.id, data_solucao = NOW(), hora_solucao = NOW() WHERE id = NEW.ticket_id;
                END IF;
                
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_mensagem_ticket_solucao ON mensagem_ticket;
        CREATE TRIGGER trg_mensagem_ticket_solucao
        AFTER INSERT ON mensagem_ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_mensagem_ticket_solucao();
    """

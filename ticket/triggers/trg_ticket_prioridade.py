def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_prioridade()
        RETURNS TRIGGER AS $$
            DECLARE
                prioridade_grupo smallint;
                prioridade_subgrupo smallint;
        
            BEGIN
                prioridade_grupo := COALESCE((SELECT prioridade FROM agrupamento WHERE id = NEW.grupo_id), 0);
                prioridade_subgrupo := COALESCE((SELECT prioridade FROM agrupamento WHERE id = NEW.subgrupo_id), 0);
            
                NEW.prioridade := prioridade_grupo + prioridade_subgrupo;
                
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_prioridade ON ticket;
        CREATE TRIGGER trg_ticket_prioridade
        BEFORE INSERT OR UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_prioridade();
    """

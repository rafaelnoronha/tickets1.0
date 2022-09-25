def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_movimento_ticket_base()
        RETURNS TRIGGER AS $$
            DECLARE data_inicio date;
            DECLARE hora_inicio time;
            DECLARE data_fim date;
            DECLARE hora_fim time;
            DECLARE ultimo_movimento record;
        
            BEGIN
                SELECT * INTO ultimo_movimento FROM movimento_ticket WHERE ticket_id = NEW.ticket_id ORDER BY ticket_id DESC LIMIT 1;

                IF (ultimo_movimento.data_inicio IS NULL AND NEW.atendente_id IS NOT NULL) THEN
                    data_inicio := now();
                    hora_inicio := now();
                ELSE
                    data_inicio := ultimo_movimento.data_inicio;
                    hora_inicio := ultimo_movimento.hora_inicio;
                END IF;

                IF (ultimo_movimento.data_fim IS NULL AND NEW.cancelado_id IS NOT NULL) THEN
                    data_fim := now();
                    hora_fim := now();
                ELSE
                    data_fim := ultimo_movimento.data_fim;
                    hora_fim := ultimo_movimento.hora_fim;
                END IF;
        
                IF (NEW.atendente_id IS NULL) THEN NEW.atendente_id := ultimo_movimento.atendente_id
                IF (NEW.cancelado_id IS NULL) THEN NEW.cancelado_id := ultimo_movimento.cancelado_id
                IF (NEW.classificacao_atendente_id IS NULL) THEN NEW.classificacao_atendente_id := ultimo_movimento.classificacao_atendente_id
                IF (NEW.finalizado_id IS NULL) THEN NEW.finalizado_id := ultimo_movimento.finalizado_id
                IF (NEW.solucao_id IS NULL) THEN NEW.solucao_id := ultimo_movimento.solucao_id
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_movimento_ticket_base ON movimento_ticket;
        CREATE TRIGGER trg_movimento_ticket_base
        BEFORE INSERT ON movimento_ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_movimento_ticket_base();
    """

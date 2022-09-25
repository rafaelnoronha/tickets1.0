def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_movimento_ticket_base()
        RETURNS TRIGGER AS $$
            DECLARE _data_inicio date;
            DECLARE _hora_inicio time;
            DECLARE _data_fim date;
            DECLARE _hora_fim time;
            DECLARE _ultimo_movimento record;
        
            BEGIN
                SELECT * INTO _ultimo_movimento FROM movimento_ticket WHERE ticket_id = NEW.ticket_id ORDER BY ticket_id DESC LIMIT 1;

                IF (_ultimo_movimento.data_inicio IS NULL AND NEW.atendente_id IS NOT NULL) THEN
                    _data_inicio := now();
                    _hora_inicio := now();
                ELSE
                    _data_inicio := _ultimo_movimento.data_inicio;
                    _hora_inicio := _ultimo_movimento.hora_inicio;
                END IF;

                IF (_ultimo_movimento.data_fim IS NULL AND NEW.cancelado_id IS NOT NULL) THEN
                    _data_fim := now();
                    _hora_fim := now();
                ELSE
                    _data_fim := _ultimo_movimento.data_fim;
                    _hora_fim := _ultimo_movimento.hora_fim;
                END IF;
        
                IF (NEW.atendente_id IS NULL) THEN NEW.atendente_id := _ultimo_movimento.atendente_id
                IF (NEW.cancelado_id IS NULL) THEN NEW.cancelado_id := _ultimo_movimento.cancelado_id
                IF (NEW.classificacao_atendente_id IS NULL) THEN NEW.classificacao_atendente_id := _ultimo_movimento.classificacao_atendente_id
                IF (NEW.finalizado_id IS NULL) THEN NEW.finalizado_id := _ultimo_movimento.finalizado_id
                IF (NEW.solucao_id IS NULL) THEN NEW.solucao_id := _ultimo_movimento.solucao_id
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_movimento_ticket_base ON movimento_ticket;
        CREATE TRIGGER trg_movimento_ticket_base
        BEFORE INSERT ON movimento_ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_movimento_ticket_base();
    """

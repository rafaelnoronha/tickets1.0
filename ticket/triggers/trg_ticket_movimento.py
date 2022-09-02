def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_movimento()
        RETURNS TRIGGER AS $$
            DECLARE data_inicio date;
            DECLARE hora_inicio time;
            DECLARE data_fim date;
            DECLARE hora_fim time;
            DECLARE ultimo_movimento record;
        
            BEGIN
                IF (TG_OP = 'INSERT') THEN
                    IF (NEW.atendente_id IS NOT NULL) THEN
                        data_inicio := now();
                        hora_inicio := now();
                    END IF;
                ELSIF (TG_OP = 'UPDATE') THEN
                    SELECT * INTO ultimo_movimento FROM movimento_ticket WHERE ticket_id = NEW.id ORDER BY ticket_id DESC LIMIT 1;
        
                    IF (OLD.atendente_id IS NULL AND ultimo_movimento.data_inicio IS NULL AND NEW.atendente_id IS NOT NULL) THEN
                        data_inicio := now();
                        hora_inicio := now();
                    ELSE
                        data_inicio := ultimo_movimento.data_inicio;
                        hora_inicio := ultimo_movimento.hora_inicio;
                    END IF;
        
                    IF (OLD.finalizado_id IS NULL AND NEW.finalizado_id IS NOT NULL OR OLD.cancelado_id IS NULL AND NEW.cancelado_id IS NOT NULL) THEN
                        data_fim := now();
                        hora_fim := now();
                    ELSE
                        data_fim := ultimo_movimento.data_fim;
                        hora_fim := ultimo_movimento.hora_fim;
                    END IF;
                END IF;
                
                IF (
                    TG_OP = 'INSERT'
                    OR OLD.atendente_id IS DISTINCT FROM NEW.atendente_id
                    OR OLD.cancelado_id IS DISTINCT FROM NEW.cancelado_id
                    OR OLD.classificacao_atendente_id IS DISTINCT FROM NEW.classificacao_atendente_id
                    OR OLD.finalizado_id IS DISTINCT FROM NEW.finalizado_id
                    OR OLD.solucionado_id IS DISTINCT FROM NEW.solucionado_id
                ) THEN
        
                    INSERT INTO movimento_ticket(
                        ativo
                        ,data_cadastro
                        ,hora_cadastro
                        ,data_inicio
                        ,hora_inicio
                        ,data_fim
                        ,hora_fim
                        ,atendente_id
                        ,cancelado_id
                        ,classificacao_atendente_id
                        ,finalizado_id
                        ,solucionado_id
                        ,ticket_id
                    ) 
                    VALUES(
                        true
                        ,now()
                        ,now()
                        ,data_inicio
                        ,hora_inicio
                        ,data_fim
                        ,hora_fim
                        ,NEW.atendente_id
                        ,NEW.cancelado_id
                        ,NEW.classificacao_atendente_id
                        ,NEW.finalizado_id
                        ,NEW.solucionado_id
                        ,NEW.id
                    );
                END IF;
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_movimento ON ticket;
        CREATE TRIGGER trg_ticket_movimento
        BEFORE INSERT OR UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_movimento();
    """

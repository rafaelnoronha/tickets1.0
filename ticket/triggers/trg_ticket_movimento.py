def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_movimento()
        RETURNS TRIGGER AS $$
            DECLARE data_inicio date;
            DECLARE hora_inicio time;
            DECLARE data_fim date;
            DECLARE hora_fim time;
        
            BEGIN
                IF (TG_OP = 'INSERT') THEN
                    IF (NEW.atendente_id IS NOT NULL) THEN
                        data_inicio := now();
                        hora_inicio := now();
                    END IF;
                ELSIF (TG_OP = 'UPDATE') THEN
                    IF (OLD.atendente_id IS NULL AND OLD.data_inicio IS NULL AND NEW.atendente_id IS NOT NULL) THEN
                        data_inicio := now();
                        hora_inicio := now();
                    ELSE
                        data_inicio := (SELECT mt.data_inicio FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                        hora_inicio := (SELECT mt.hora_inicio FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                    END IF;
        
                    IF (OLD.finalizado_id IS NULL AND NEW.finalizado_id IS NOT NULL OR OLD.cancelado_id IS NULL AND NEW.cancelado_id IS NOT NULL) THEN
                        data_fim := now();
                        hora_fim := now();
                    ELSE
                        data_fim := (SELECT mt.data_fim FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                        hora_fim := (SELECT mt.hora_fim FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                    END IF;
                END IF;
        
                INSERT INTO movimento_ticket(
                    uuid
                    ,ativo
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
                    uuid_generate_v4()
                    ,true
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
        
                RETURN NEW;
            END
        $$ LANGUAGE plpgsql;
        
        DROP TRIGGER IF EXISTS trg_ticket_movimento ON ticket;
        CREATE TRIGGER trg_ticket_movimento
        BEFORE INSERT OR UPDATE ON ticket
        FOR EACH ROW EXECUTE PROCEDURE trg_ticket_movimento();
    """

    """
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
                ultimo_movimento := (SELECT * FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                
                IF (OLD.atendente_id IS NULL AND OLD.data_inicio IS NULL AND NEW.atendente_id IS NOT NULL) THEN
                    data_inicio := now();
                    hora_inicio := now();
                ELSE
                    data_inicio := (SELECT mt.data_inicio FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                    hora_inicio := (SELECT mt.hora_inicio FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                END IF;
    
                IF (OLD.finalizado_id IS NULL AND NEW.finalizado_id IS NOT NULL OR OLD.cancelado_id IS NULL AND NEW.cancelado_id IS NOT NULL) THEN
                    data_fim := now();
                    hora_fim := now();
                ELSE
                    data_fim := (SELECT mt.data_fim FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                    hora_fim := (SELECT mt.hora_fim FROM movimento_ticket AS mt WHERE mt.ticket_id = NEW.id ORDER BY mt.ticket_id DESC LIMIT 1);
                END IF;
            END IF;
    
            INSERT INTO movimento_ticket(
                uuid
                ,ativo
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
                uuid_generate_v4()
                ,true
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
    
            RETURN NEW;
        END
    $$ LANGUAGE plpgsql;
    
    DROP TRIGGER IF EXISTS trg_ticket_movimento ON ticket;
    CREATE TRIGGER trg_ticket_movimento
    BEFORE INSERT OR UPDATE ON ticket
    FOR EACH ROW EXECUTE PROCEDURE trg_ticket_movimento();
    """

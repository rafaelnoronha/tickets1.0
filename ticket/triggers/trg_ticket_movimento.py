def trigger():
    return """
        CREATE OR REPLACE FUNCTION trg_ticket_movimento()
        RETURNS TRIGGER AS $$
            DECLARE data_fim date;
            DECLARE hora_fim time;
        
            BEGIN
                IF (NEW.data_cancelamento) THEN
                    data_fim := NEW.data_cancelamento;
                    hora_fim := NEW.hora_cancelamento;
                ELSE
                    data_fim = NEW.data_finalizacao;
                    hora_fim = NEW.hora_finalizacao;
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
                    ,NEW.data_atribuicao_atendente
                    ,NEW.hora_atribuicao_atendente
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

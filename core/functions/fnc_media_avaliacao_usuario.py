def function():
    return """
        CREATE OR REPLACE FUNCTION fnc_media_avaliacao_atendente(usuario_id bigint)
        RETURNS numeric AS $$
            BEGIN
                RETURN (
                    SELECT
                        (COALESCE(SUM(avaliacao_solicitante), 0) / COALESCE(COUNT(id), 0))
                    FROM ticket 
                    WHERE atendente_id = usuario_id
                    AND finalizado_id IS NOT NULL
                    AND avaliacao_solicitante IS NOT NULL
                );
            END
        $$ LANGUAGE plpgsql;
    """
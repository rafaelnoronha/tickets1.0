def function():
    return """
        CREATE OR REPLACE FUNCTION fnc_media_avaliacao_atendente(usuario_id bigint)
        RETURNS numeric AS $$
            BEGIN
                RETURN (
                    SELECT
                        CAST(CAST(SUM(avaliacao_solicitante) AS numeric) / COALESCE(COUNT(id), 0) AS numeric(2,1))
                    FROM ticket 
                    WHERE atendente_id = usuario_id
                    AND finalizado_id IS NOT NULL
                    AND avaliacao_solicitante IS NOT NULL
                );
            END
        $$ LANGUAGE plpgsql;
    """
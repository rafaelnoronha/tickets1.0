def function():
    return """
        CREATE OR REPLACE FUNCTION fnc_media_avaliacao_empresa(empresa_id bigint)
        RETURNS numeric AS $$
            BEGIN
                RETURN (
                    SELECT
                        CAST((CAST(SUM(tk.avaliacao_solicitante) AS numeric)) / COUNT(tk.id) AS numeric(2,1))
                    FROM ticket AS tk
                        LEFT JOIN usuario AS us ON us.id = tk.atendente_id
                    WHERE 
                        us.empresa_id = empresa_id
                    AND finalizado_id IS NOT NULL
                    AND avaliacao_solicitante IS NOT NULL
                );
            END
        $$ LANGUAGE plpgsql;
    """
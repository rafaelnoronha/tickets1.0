def function():
    return """
        CREATE OR REPLACE FUNCTION fnc_media_avaliacao_usuario(usuario_id bigint, solicitante bool)
        RETURNS integer AS $$
            BEGIN
                IF (solicitante) THEN
                    RETURN (SELECT (COALESCE(SUM(avaliacao_atendente), 0) / COALESCE(COUNT(id), 0)) FROM ticket 
                        WHERE solicitante_id = usuario_id AND finalizado_id IS NOT NULL AND avaliacao_atendente IS NOT NULL);
                ELSE 
                    RETURN (SELECT (COALESCE(SUM(avaliacao_solicitante), 0) / COALESCE(COUNT(id), 0)) FROM ticket 
                        WHERE atendente_id = usuario_id AND finalizado_id IS NOT NULL AND avaliacao_solicitante IS NOT NULL);
                END IF;
            END
        $$ LANGUAGE plpgsql;
    """
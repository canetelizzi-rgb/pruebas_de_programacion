from datos import obtener_eventos


def normalizar_fecha(fecha):
    return fecha.strip()


def buscar_eventos_por_fecha(fecha):
    fecha_normalizada = normalizar_fecha(fecha)
    todos_los_eventos = obtener_eventos()

    eventos_encontrados = []
    for evento in todos_los_eventos:
        if evento["fecha"] == fecha_normalizada:
            eventos_encontrados.append(evento)

    return eventos_encontrados
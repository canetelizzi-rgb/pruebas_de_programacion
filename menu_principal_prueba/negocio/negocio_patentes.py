from datos import obtener_vehiculos


def normalizar_patente(patente):
    return patente.strip().upper()


def buscar_vehiculo_por_patente(patente):
    patente_normalizada = normalizar_patente(patente)
    vehiculos = obtener_vehiculos()

    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente_normalizada:
            return vehiculo

    return None
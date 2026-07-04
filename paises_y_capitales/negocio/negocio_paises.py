from datos import obtener_capital


def normalizar(texto):
    return texto.strip().lower()


def buscar_capital(pais):
    pais_normalizado = normalizar(pais)
    capital = obtener_capital(pais_normalizado)
    return pais_normalizado.title(), capital
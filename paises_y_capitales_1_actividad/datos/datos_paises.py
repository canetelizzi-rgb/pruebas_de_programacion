paises_capitales = {
    "chile": "Santiago",
    "argentina": "Buenos Aires",
    "peru": "Lima",
    "colombia": "Bogotá",
    "mexico": "Ciudad de México",
    "españa": "Madrid",
    "brasil": "Brasilia",
    "ecuador": "Quito",
    "bolivia": "Sucre",
    "uruguay": "Montevideo",
    "paraguay": "Asunción",
    "venezuela": "Caracas",
    "francia": "París",
    "italia": "Roma",
    "alemania": "Berlín",
}


def obtener_capital(pais_normalizado):
    """
    Retorna la capital de un país normalizado.
    Si el país no existe como clave del diccionario, Python lanza
    automáticamente un KeyError.
    """
    return paises_capitales[pais_normalizado]
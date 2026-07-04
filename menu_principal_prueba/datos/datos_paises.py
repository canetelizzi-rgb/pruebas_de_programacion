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
    return paises_capitales[pais_normalizado]
from negocio import buscar_capital


def iniciar():
    print("BÚSQUEDA DE CAPITAL SEGÚN PAÍS")

    pais = input("Ingrese el nombre del país: ")

    try:
        pais_formateado, capital = buscar_capital(pais)
        print(f"La capital de {pais_formateado} es: {capital}")
    except KeyError:
        print(f"No se encontró el país '{pais.strip().title()}' en la base de datos.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
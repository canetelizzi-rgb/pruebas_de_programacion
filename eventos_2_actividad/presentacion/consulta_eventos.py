from negocio import buscar_eventos_por_fecha


def iniciar():
    print("   CONSULTA DE EVENTOS POR FECHA")

    fecha = input("Ingrese la fecha a consultar (dd/mm/aaaa): ")

    try:
        eventos_encontrados = buscar_eventos_por_fecha(fecha)

        if eventos_encontrados:
            print(f"Eventos programados para el {fecha.strip()}:")
            for evento in eventos_encontrados:
                print(f"  - {evento['nombre']} en {evento['lugar']}")
        else:
            print(f"No hay eventos programados para el {fecha.strip()}.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
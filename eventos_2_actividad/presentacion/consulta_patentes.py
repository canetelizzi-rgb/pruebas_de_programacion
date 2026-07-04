from negocio import buscar_vehiculo_por_patente


def iniciar_consulta_patentes():
    print("   CONSULTA DE VEHÍCULO POR PATENTE")

    patente = input("Ingrese la patente a consultar: ")

    try:
        vehiculo = buscar_vehiculo_por_patente(patente)

        if vehiculo:
            print(f"Vehículo encontrado:")
            print(f"  Patente:     {vehiculo['patente']}")
            print(f"  Marca:       {vehiculo['marca']}")
            print(f"  Modelo:      {vehiculo['modelo']}")
            print(f"  Año:         {vehiculo['anio']}")
            print(f"  Color:       {vehiculo['color']}")
            print(f"  Propietario: {vehiculo['propietario']}")
        else:
            print(f"No se encontró ningún vehículo con la patente '{patente.strip().upper()}'.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
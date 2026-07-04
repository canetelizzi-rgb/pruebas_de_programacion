from presentacion.busqueda_capital import iniciar_busqueda_capital
from presentacion.consulta_eventos import iniciar_consulta_eventos
from presentacion.consulta_patentes import iniciar_consulta_patentes


def menu_principal():
    print("SISTEMA DE CONSULTAS")

    while True:
        print("Seleccione una opción:")
        print("1. Buscar la capital de un país")
        print("2. Consultar eventos por fecha")
        print("3. Consultar vehículo por patente")
        print("0. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            iniciar_busqueda_capital()
        elif opcion == "2":
            iniciar_consulta_eventos()
        elif opcion == "3":
            iniciar_consulta_patentes()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
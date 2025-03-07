msj_bienvenida = """ Bienvenido al taller mecánico Iconic. Este programa gestiona el inventario de coches. """
inventario = "Este es el inventario actual de carros:"
opciones = """ Acciones: 
1) Agregar un carro 
2) Eliminar un carro 
3) Ordenar el inventario 
4) Salir """
agregar_coche = """ Ingresa el coche que deseas agregar: """
eliminar_coche = """ Ingresa el coche que deseas eliminar: """
coche_agg = """ El coche fue agregado:"""
opc_invalida = """ La opción que ingresaste es inválida."""
despedida = """ Gracias por usar este programa para la gestión del taller Iconic. 
Este programa fue creado por Jose Mauricio Perales Ramos El Empírico."""

coches = ["Mclaren720", "Ferrari SF90", "Aventador SVJ", "Taycan", "Urus", "Phantom"]

def iniciar_taller():
    print(msj_bienvenida)
    print(inventario)
    for coche in coches:
        print(coche.title())

    while True:
        print(opciones)
        opc = input("Dime qué opción deseas realizar: ").strip()

        if opc == "1":
            # Agregar carro
            while True:
                coche = input(agregar_coche).strip()
                if coche:
                    coches.append(coche)
                    print(coche_agg, coche)
                    print(inventario)
                    for coche in coches:
                        print(coche.title())
                    break
                else:
                    print(opc_invalida)

        elif opc == "2":
            # Eliminar coche
            while True:
                coche = input(eliminar_coche).strip()
                if coche:
                    if coche in coches:
                        coches.remove(coche)
                        print("El coche fue eliminado.")
                        print(inventario)
                        for coche in coches:
                            print(coche.title())
                        break
                    else:
                        print("El modelo ingresado no está en el inventario.")
                else:
                    print(opc_invalida)

        elif opc == "3":
            # Ordenar inventario
            coches.sort()
            print("Inventario ordenado:")
            for coche in coches:
                print(coche.title())

        elif opc == "4":
            # Salir del programa
            print(despedida)
            break

        else:
            print(opc_invalida)

if __name__ == "__main__":
    iniciar_taller()

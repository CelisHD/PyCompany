
import funciones

while True:

    print("Gestion Interna PyCompany \nMenú de opciones:")
    print("1. Registrar la informacion de un empleado")
    print("2. Calcular bono empleado") 
    print("3. Mostrar el resumen del trabajdor")
    print("4. Salir del programa")

    opcion = funciones.ingresarEntero("Selecciona una opción (1-4): ")

    if opcion in [1, 2, 3]:

        match opcion:
            
            case 1:
                print("Opción 1 seleccionada: Registrar la información de un empleado.\n")
            case 2:
                print("Opción 2 seleccionada: Calcular bono empleado.\n")
            case 3:
                print("Opción 3 seleccionada: Mostrar el resumen del trabajador.\n")
        
            
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
        
False

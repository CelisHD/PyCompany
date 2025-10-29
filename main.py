import funciones

# ---- Funciones principales del programa ---- 

def menu_principal():
    print("Bienvenido a la Gestión Interna de PyCompany")
    print("-------------------------------------------")
    print("Seleccione una opción del menú:")
    print("1. Registrar la información de un empleado")
    print("2. Calcular bono empleado")
    print("3. Mostrar el resumen del trabajador")
    print("4. Salir del programa")

# ---- Lógica del programa ----

while True:

    menu_principal()
    opcion = funciones.ingresarEntero("Selecciona una opción (1-4): ")

    match opcion:

        case 1:
            print("Opción 1 seleccionada: Registrar la información de un empleado.\n")
        case 2:
            print("Opción 2 seleccionada: Calcular bono empleado.\n")
        case 3:
            print("Opción 3 seleccionada: Mostrar el resumen del trabajador.\n")
        
        case 4:
            print("Este ejercicio no es solo para programar: es para trabajar en equipo, coordinarse, revisar código y aprender de los errores. La clave no es hacerlo perfecto, sino **hacerlo juntos** y **entender cómo se arma un programa completo paso a paso.** 🚀")
            print("\nSaliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")
        


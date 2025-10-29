import funciones
import datos
import bono
import resumen

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
            nombre, edad, cargo, sueldo_base, porcentaje_bono = datos.obtener_datos_usuario()
            print(f"\nInformación del empleado {nombre} registrada con éxito.\n")

        case 2:
            total = bono.calcular_bono(sueldo_base, porcentaje_bono)
            print(f"\nEl salario total con bono es: {total}\n")

        case 3:
            resumen.mostrar_resumen(nombre, edad, cargo, sueldo_base, porcentaje_bono)
        
        case 4:
            print("Este ejercicio no es solo para programar: es para trabajar en equipo, coordinarse, revisar código y aprender de los errores. La clave no es hacerlo perfecto, sino **hacerlo juntos** y **entender cómo se arma un programa completo paso a paso.** 🚀")
            print("\nSaliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")
        


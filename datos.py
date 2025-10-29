# ---- funcion para obtener datos del usuario -----
def obtener_datos_usuario():
    nombre = input(" ingresa tu nombre:")
    edad = int(input(" ingresa tu edad:"))
    cargo = input(" ingresa tu cargo:")
    sueldo_base = float(input(" ingrea su sueldo base :"))
    porcentaje_bono = float(input("ingrese el porcentaje del bono (%)"))
    
    return nombre, edad, cargo, sueldo_base, porcentaje_bono

# DATOS DEL USUARIO

# nombre = input(" ingresa tu nombre:")
# edad = int(input(" ingresa tu edad:"))
# cargo = input(" ingresa tu cargo:")
# sueldo_base = float(input(" ingrea su sueldo base :"))
# porcentaje_bono = float(input("ingrese el porcentaje del bono (%)"))

# print(f"nombre: {nombre}")
# print(f"edad: {edad}")
# print(f"cargo: {cargo}")
# print(f"sueldo_base: {sueldo_base}")
# print (f"porcentaje_bono: {porcentaje_bono}")
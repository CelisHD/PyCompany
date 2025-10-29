def ingresarEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero entero.")

def intresarDecimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero.")

def ingresarTexto(mensaje):
    valor = input(mensaje)
    return valor
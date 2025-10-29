# ------ funciond calcular bono -----

def calcular_bono(sueldo_base: float, porcentaje: float) -> float:
  
    bono = sueldo_base * (porcentaje / 100)
    total = sueldo_base + bono
    return total


# bono.py

# def calcular_bono(sueldo_base: int, porcentaje: float) -> float:
  
#     bono = sueldo_base * (porcentaje / 100)
#     total = sueldo_base + bono
#     return total

"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Cociente y residuo
=========================================
Fecha: 24 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def division(dividendo, divisor):
    """ Calcula el cociente y el residuo de dos números.
    (int, int) -> (int, int) """
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    residuo = dividendo
    return cociente, residuo

def main():
    dividendo = int(input("Ingresa el dividendo: "))
    divisor = int(input("Ingresa el divisor: "))
    
    if dividendo > 0 and divisor > 0:
        cociente, residuo = division(dividendo, divisor)
        print(f"Cociente: {cociente}")
        print(f"Residuo: {residuo}")
    else:
        print("Ambos números deben ser mayores que 0.")
main()
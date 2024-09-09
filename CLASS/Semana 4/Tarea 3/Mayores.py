"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Números mayores que 100
=========================================
Fecha: 3 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def es_mayor_100(num):
    """ Verifica si un número es mayor a 100
    (int) -> int
    """
    return num > 100

def mayores_100(n1, n2, n3):
    """Devuelve una cadena de numero separados por comas
    (int, int, int) -> int, int, int
    """
    value = []
    if es_mayor_100(n1):
        value.append(str(n1))
    if es_mayor_100(n2):
        value.append(str(n2))
    if es_mayor_100(n3):
        value.append(str(n3))
    
    if value:
        return ','.join(value)
    else:
        return "Ninguno es mayor que 100"

def main():
    """ Permite el ingreso de datos """
    n1 = int(input('Ingrese un primer número diferente de cero: '))
    n2 = int(input('Ingrese un segundo número diferente de cero: '))
    n3 = int(input('Ingrese un tercer número diferente de cero: '))

    """ Comprueba si los números son diferentes de cero """
    if n1 != 0 and n2 != 0 and n3 != 0:
        resultado = mayores_100(n1, n2, n3)
        print("Resultado:", resultado)
    else:
        print("Error: Todos los números deben ser diferentes de cero.")

main()

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
def mayores_100(n1, n2, n3):
    """
    Nos permite saber si los números son mayores a 100
    """
    r1, r2, r3 = None, None, None
    
    if n1 > 100:
        r1 = n1

    if n2 > 100:
        r2 = n2

    if n3 > 100:
        r3 = n3

    if r1 and r2 and r3:
        return f"{r1},{r2},{r3}"
    elif r1 and r2:
        return f"{r1},{r2}"
    elif r1 and r3:
        return f"{r1},{r3}"
    elif r2 and r3:
        return f"{r2},{r3}"
    elif r1:
        return str(r1)
    elif r2:
        return str(r2)
    elif r3:
        return str(r3)
    else:
        return "Ningún número es mayor que 100"

def main():
    """
    Permite el ingreso de los tres números
    También comprueba si los números son diferentes de cero
    """
    n1 = int(input('Ingrese un primer número diferente de cero: '))
    if n1 == 0:
        print("Error: El primer número no puede ser cero.")
        return
    
    n2 = int(input('Ingrese un segundo número diferente de cero: '))
    if n2 == 0:
        print("Error: El segundo número no puede ser cero.")
        return
    
    n3 = int(input('Ingrese un tercer número diferente de cero: '))
    if n3 == 0:
        print("Error: El tercer número no puede ser cero.")
        return

    r = mayores_100(n1, n2, n3)
    print(r)

main()
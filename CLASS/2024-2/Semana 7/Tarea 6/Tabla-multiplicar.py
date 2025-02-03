"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Tabla de multiplicar
=========================================
Fecha: 24 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def tabla_recurrente(n, cont=1):
    """ Imprime la tabla de multiplicar del número n usando recursión.
    (int, int) -> None """

    if cont > 10:
        return
    else:
        print(f"{n} x {cont} = {n * cont}")
        tabla_recurrente(n, cont + 1)

def main():
    n = int(input("Ingresa un número entero positivo: "))
    if n > 0:
        tabla_recurrente(n)
    else:
        print("El número debe ser mayor que 0.")
main()

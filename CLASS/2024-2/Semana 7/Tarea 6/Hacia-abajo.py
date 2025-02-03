"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Hacia abajo
=========================================
Fecha: 24 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def s_recurrencia(n):
    """ Proporciona una serie descendiente segun el valor elegido por el usuario
    (int) -> None """
    if n <= 0:
        return
    else:
        print(str(n) * n)
        s_recurrencia(n - 1)

def main():
    n = int(input("Ingresa un número entero positivo: "))
    if n > 0:
        s_recurrencia(n)
    else:
        print("El número debe ser mayor que 0.")
main()


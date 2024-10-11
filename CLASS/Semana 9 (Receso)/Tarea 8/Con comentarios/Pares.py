"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Pares
=========================================
Fecha: 10 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def pares(a, b):
    """Genera la secuencia de pares en el intervalo cerrado [a,b]. a <= b
       (int, int) -> list"""
    # Creamos una lista vacía para almacenar los números pares
    pares = []
    # Iteramos desde a hasta b (inclusive)
    for num in range(a, b + 1):
        # Verificamos si el número es par
        if num % 2 == 0:
            pares.append(num)
    return pares

def main():
    # Pedimos al usuario que ingrese los valores de a y b separados por comas
    entrada = input("Ingresa los valores de a y b (separados por comas): ")
    # Convertimos la cadena de entrada en dos enteros
    a, b = map(int, entrada.split(','))
    # Llamamos a la función pares para obtener la lista de pares
    resultado = pares(a, b)
    # Imprimimos la lista de pares o "Vacía" si no hay pares
    if resultado:
        print(",".join(map(str, resultado)))
    else:
        print("Vacía")

# Llamamos a la función principal para ejecutar el programa
main()
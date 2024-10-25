"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Suma filas
=========================================
Fecha: 22 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""

def suma_filas(matriz):
    """ 
    Función para sumar los valores de cada fila de una matriz.
    (list de dos dimensiones) -> list de una dimensión
    """
    # Crea una lista vacía para almacenar las sumas de cada fila
    resultado = []
    
    # Itera sobre cada fila de la matriz
    for fila in matriz:
        # Sumar todos los elementos de la fila actual
        suma_fila = sum(fila)
        # Agrega la suma de la fila a la lista de resultados
        resultado.append(suma_fila)
    
    return resultado

def main():
    m, n = map(int, input().split(','))

    # Inicializa una lista vacía para almacenar la matriz
    matriz = []
    # Repite el siguiente bloque m veces (una vez por cada fila)
    for _ in range(m):
        # Lee una fila, separa los números por comas y los convierte a enteros
        fila = list(map(int, input().split(',')))
        # Agrega la fila a la matriz
        matriz.append(fila)
    
    # Llama a la función suma_filas y almacena el resultado
    suma_filas(matriz)
    resultado = suma_filas(matriz)
    
    # Convierte cada suma a cadena y las une con comas para imprimir
    # .join nos ayuda a concatenar los elementos de la lista en una cadena
    # map nos ayuda a convertir cada elemento a string
    print(",".join(map(str, resultado)))

main()
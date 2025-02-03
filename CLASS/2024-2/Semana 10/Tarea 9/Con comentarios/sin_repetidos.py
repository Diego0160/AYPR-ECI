"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Sin Repetidos
=========================================
Fecha: 22 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def sin_repetidos(arr):
    """ Función para eliminar repeticiones en una lista
    (list) -> list"""

    # Verificamos que la lista no esté vacía
    if len(arr) == 0:
        return []
    
    # Inicializamos la lista de resultado con el primer elemento
    resultado = [arr[0]]
    
    # Usamos un ciclo for para recorrer la lista
    for i in range(1, len(arr)):
        # Verificamos si el elemento actual es diferente al anterior
        if arr[i] != arr[i-1]:
            resultado.append(arr[i])
    
    return resultado

def main():
    # Solicitamos la secuencia al usuario
    # Split nos ayuda con la separación de los elementos

    entrada = input().split()
    
    # Convertimos la entrada a enteros
    entrada = [int(x) for x in entrada]
    
    # Llamamos a la función y obtenemos la lista
    sin_repetidos(entrada)
    salida = sin_repetidos(entrada)
    
    # Mostramos el resultado como una cadena de números separados por espacio
    # .join nos ayuda a concatenar los elementos de la lista en una cadena
    # map nos ayuda a convertir cada elemento a string
    print(" ".join(map(str, salida)))

main()
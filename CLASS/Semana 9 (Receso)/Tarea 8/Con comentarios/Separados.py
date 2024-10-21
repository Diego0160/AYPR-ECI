"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Separados
=========================================
Fecha: 10 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def clasificar_numero(num, positivos, negativos, ceros):
    """Clasifica un número en una de las tres listas: positivos, negativos o ceros.
       (int, list, list, list) -> None"""
    if num > 0:
        positivos.append(num)
    elif num < 0:
        negativos.append(num)
    else:
        ceros.append(num)

def separar_numeros(secuencia):
    """Separa los números en tres listas: positivos, negativos y ceros.
       (str) -> tuple"""
    # Convertimos la secuencia de números a una lista de enteros
    numeros = list(map(int, secuencia.split(',')))
    positivos = []
    negativos = []
    ceros = []

    # Iteramos sobre la lista de números y usamos clasificar_numero
    for num in numeros:
        clasificar_numero(num, positivos, negativos, ceros)

    return positivos, negativos, ceros

def main():
    # Pedimos al usuario que ingrese la secuencia de números enteros separados por comas
    entrada = input("Ingresa la secuencia de números enteros separados por comas: ")
    # Llamamos a la función separar_numeros para obtener las tres listas
    positivos, negativos, ceros = separar_numeros(entrada)
    
    # Imprimimos las listas resultantes
    if positivos:
        print("Positivos:", ",".join(map(str, positivos)))
    if negativos:
        print("Negativos:", ",".join(map(str, negativos)))
    if ceros:
        print("Ceros:", ",".join(map(str, ceros)))

# Llamamos a la función principal para ejecutar el programa
main()
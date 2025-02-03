"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Invertir
=========================================
Fecha: 10 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def invertir(elementos):
    """Invierte los elementos de una lista
       n > 0
       (list) -> list"""
    cantidad = len(elementos)
    # Invertimos los elementos en la misma lista
    for i in range(cantidad // 2):
        elementos[i], elementos[cantidad - i - 1] = elementos[cantidad - i - 1], elementos[i]
    return elementos

def main():
    # Pedimos al usuario que ingrese los elementos separados por comas
    entrada = input("Ingresa los elementos separados por comas: ")
    # Convertimos la cadena de entrada en una lista de elementos
    elementos = entrada.split(',')
    # Llamamos a la función invertir para obtener la lista invertida
    arreglo_invertido = invertir(elementos)
    # Imprimimos la lista invertida de forma correcta
    print(','.join(arreglo_invertido))

# Llamamos a la función principal para ejecutar el programa
main()
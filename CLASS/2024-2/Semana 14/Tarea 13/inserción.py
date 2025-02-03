"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Ordenamiento por inserción
===========================================
Fecha: 19 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def ordenamiento_insercion(lista):
    """ Ordena una lista usando el método de inserción y muestra el proceso paso a paso.
    (list) -> None
    """
    numeros = [int(x) for x in lista]

    for i in range(1, len(numeros)):
        numero_actual = numeros[i]
        print(f"Numero enfocado: {numero_actual}")

        j = i - 1
        desplazamientos = False

        while j >= 0 and numeros[j] > numero_actual:
            if not desplazamientos:
                print(f"Desplaza -> {numeros[j]}")
            desplazamientos = True
            numeros[j + 1] = numeros[j]
            j -= 1

        if not desplazamientos:
            print("Sin desplazamientos")
        
        numeros[j + 1] = numero_actual
        print(f"Inserta: {numero_actual}")
        print(numeros)

def main():
    entrada = input()
    lista = entrada.split()
    
    ordenamiento_insercion(lista)

main()
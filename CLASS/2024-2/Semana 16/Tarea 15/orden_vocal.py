"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Vocales en orden
===========================================
Fecha: 3 de Diciembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def contar_vocales(palabra):
    """ Cuenta la cantidad de vocales en una palabra.
    (str) -> int """
    vocales = 'aeiou'
    contador = 0
    for letra in palabra.lower():
        if letra in vocales:
            contador += 1
    return contador

def clave_ordenamiento(palabra):
    """ Genera una clave para ordenar las palabras según las reglas especificadas.
    (str) -> tuple """
    return (contar_vocales(palabra), len(palabra))


def ordenar_por_vocales(palabras):
    """ Ordena una lista de palabras según la cantidad de vocales, su longitud, y el orden original.
    (list) -> list """
    return sorted(palabras, key=clave_ordenamiento)


def main():
    n = int(input())
    palabras = [input() for _ in range(n)]
    palabras_ordenadas = ordenar_por_vocales(palabras)
    print(",".join(palabras_ordenadas))

main()
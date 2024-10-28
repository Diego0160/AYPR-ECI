"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Parcial Segundo Tercio
=========================================
Fecha: 24 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def lista_par(v, n):
    """ Imprime los numeros que se encuentran en una ubicación par de una lista.
    Ej: [0, 2, 4 ...]
    (int, list) -> list"""
    pos1 = []
    count = 0
    while count <= v:
        for n in range (count):
            pos1.append(n)
        count += 2

    return pos1

def es_impar(v, n):
    """ Verifica si los numeros de la lista actual son impares para luego ser añadidos a otra lista
    (int, list) -> list"""
    pos2 = []

    for n in range (v):
        if n % 2 == 0:
            pos2.append(n)
    return pos2

def main():
    n = input().split(',')
    v = len(n)
    lista_par(v, n)
    list1 = lista_par(v, n)
    es_impar(v, n)
    list2 = es_impar(v, n)
    print(",".join(map(str, list1)))
    print(",".join(map(str, list2)))
    
main()
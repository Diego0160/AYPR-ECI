"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Intersección
=========================================
Fecha: 22 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def intersection(n1, n2):
    """ Función para encontrar la intersección de dos secuencias
    (str, str) -> list
    """
    interseccion = []
    n1 = [int(x) for x in n1]
    n2 = [int(x) for x in n2]
    
    for num in n1:
        if num in n2 and num not in interseccion:
            interseccion.append(num)
    
    interseccion.sort()
    return interseccion

def main():
    n1 = input().split(',')
    n2 = input().split(',')
    
    intersection(n1, n2)
    ans = intersection(n1, n2)
    
    if ans:
        print(" ".join(map(str, ans)))
    else:
        print("Vacia")

main()

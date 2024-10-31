"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: 
=========================================
Fecha: 31 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
# Correciones del punto 3, 5 y mejor simplificacion al main()
def secuencia_valores(v):
    """ Imprime los valores de la lista en una sola línea, separados por espacios.
    (list) -> None """
    print("Punto 2")
    print(" ".join(v))

def linea(lista):
    """ Imprime cada valor de la lista en una línea separada.
    (list) -> None """
    print("Punto 3")
    for v in lista:
        print(v)

def cantidad_elementos(lista):
    """ Devuelve la cantidad de elementos en la lista.
    (list) -> int """
    print("Punto 4")
    return len(lista)

def cantidad_pares(lista):
    """ Devuelve la cantidad de elementos pares en la lista.
    (list) -> int """
    print("Punto 5")
    count = 0
    for v in lista:
        if int(v) % 2 == 0:
            count += 1
    return count

def main():
    valores = input()
    lista = valores.split(",")
    print("Punto 1")
    print(lista)

    secuencia_valores(lista)
    linea(lista)

    
    elementos = cantidad_elementos(lista)
    print(elementos)

    
    pares = cantidad_pares(lista)
    print(pares)

main()
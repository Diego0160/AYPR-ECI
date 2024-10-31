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
def secuencia_valores(v):
    """(list) -> None
    Imprime los valores de la lista en una sola línea, separados por espacios.
    """
    print("Punto 2")
    print(" ".join(v))

def linea(lista):
    """(list) -> None
    Imprime cada valor de la lista en una línea separada.
    """
    print("Punto 3")
    for v in lista:
        print(v)

def cantidad_e(lista):
    """(list) -> int
    Devuelve la cantidad de elementos en la lista.
    """
    print("Punto 4")
    return len(lista)

def cantidad_pares(lista):
    """(list) -> int
    Devuelve la cantidad de elementos pares en la lista.
    """
    print("Punto 5")
    count = 0
    for v in lista:
        if int(v) % 2 == 0:
            count += 1
    return count

def main():
    
    valores = input("Ingrese los valores separados por coma: ")
    lista = valores.split(",")
    print("Punto 1")
    print(lista)

    
    secuencia_valores(lista)

    
    linea(lista)

    
    cantidad = cantidad_e(lista)
    print("Cantidad de elementos:", cantidad)

    
    pares = cantidad_pares(lista)
    print("Cantidad de valores pares:", pares)

main()
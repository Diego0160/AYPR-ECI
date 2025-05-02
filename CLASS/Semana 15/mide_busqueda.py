"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Midiendo tiempos de búsqueda
===========================================
Fecha: 28 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def generar_lista(t):
    """ Genera una lista con valores aleatorios entre 0 y tamaño * 3.
    (int) -> list
    """
    return [(t * 3 - i) for i in range(t)]

def busqueda_lineal(lista, valor):
    """ Realiza una búsqueda lineal en la lista.
    (list, int) -> tuple
    """
    time = 0
    for i in range(len(lista)):
        time += 1
        if lista[i] == valor:
            return i, time
    return -1, time

def busqueda_binaria(lista, valor):
    """ Realiza una búsqueda binaria en la lista (la lista debe estar ordenada).
    (list, int) -> tuple
    """
    inicio, fin = 0, len(lista) - 1
    time = 0
    
    while inicio <= fin:
        time += 1
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return medio, time
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return -1, time

def medir_tiempos_busqueda(lista, valor):
    """ Mide los time de búsqueda lineal y binaria y muestra los resultados.
    (list, int) -> None
    """
    time_lineal = busqueda_lineal(lista, valor)

    lista_ordenada = sorted(lista)
    time_binaria = busqueda_binaria(lista_ordenada, valor)
    
    print(f"\nBúsqueda Lineal: {time_lineal}")
    print(f"Búsqueda Binaria: {time_binaria}")

def main():
    t = int(input("Ingrese el tamaño de la lista: "))
    
    lista = generar_lista(t)
    print(f"Lista generada: {lista}")
    
    valor = int(input("Ingrese el valor a buscar: "))
    
    medir_tiempos_busqueda(lista, valor)
main()
"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Midiendo tiempos de ordenamiento
===========================================
Fecha: 28 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def merge_sort(lista):
    """ Implementa el algoritmo de ordenamiento Merge Sort y cuenta time.
    (list) -> tuple """
    if len(lista) <= 1:
        return lista, 0

    medio = len(lista) // 2
    izq, time_izq = merge_sort(lista[:medio])
    der, time_der = merge_sort(lista[medio:])

    fusion, time_fusion = fusionar(izq, der)
    return fusion, time_izq + time_der + time_fusion

def fusionar(izq, der):
    """ Fusiona dos listas ordenadas en una sola lista ordenada y cuenta time.
    (list, list) -> tuple """
    resultado = []
    i = j = time = 0

    while i < len(izq) and j < len(der):
        time += 1
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1


    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    time += len(izq) - i + len(der) - j
    return resultado, time

def insertion_sort(lista):
    """ Implementa el algoritmo de ordenamiento Insertion Sort y cuenta time.
    (list) -> tuple """
    time = 0
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
            time += 1
        lista[j + 1] = clave
        time += 1   
    return lista, time

def medir_time(lista):
    """ Mide y compara el número de time de ejecución de Merge Sort e Insertion Sort.
    (list) -> None """
    time_merge = merge_sort(lista[:])

    time_insertion = insertion_sort(lista[:])

    print(f"Merge Sort: {time_merge}")
    print(f"Insertion Sort: {time_insertion}")

def main():
    lista = list(map(int, input().strip().split(",")))
    
    medir_time(lista)
main()


# En consola CMD:
# python mide_tiempos.py < datos1.in
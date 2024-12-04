"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Búsqueda binaria
===========================================
Fecha: 3 de Diciembre de 2024
Autor: Diego Prado Pardo
===========================================
"""

def busqueda_binaria(lista, objetivo):
    """ Realiza una búsqueda binaria en una lista ordenada y muestra el paso a paso.
    (list, int) -> None """
    inicio = 0
    fin = len(lista) - 1
    paso = 1  # Para rastrear los pasos

    print(f"Lista: {lista}")
    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = lista[medio]

        print(f"Paso {paso}: Índice medio {medio}, valor en el medio: {valor_medio}")

        if valor_medio == objetivo:
            print(f"Valor {objetivo} encontrado en el índice {medio}")
            return
        elif valor_medio < objetivo:
            print(f"Valor buscado {objetivo} es mayor que {valor_medio}, ajustar el rango a {lista[medio + 1:fin + 1]}")
            inicio = medio + 1
        else:
            print(f"Valor buscado {objetivo} es menor que {valor_medio}, ajustar el rango a {lista[inicio:medio]}")
            fin = medio - 1

        paso += 1

    print(f"Valor {objetivo} no encontrado")


def main():
    lista = list(map(int, input().split()))
    objetivo = int(input())

    busqueda_binaria(lista, objetivo)

main()
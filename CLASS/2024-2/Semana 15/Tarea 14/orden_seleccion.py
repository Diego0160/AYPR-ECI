"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Ordenamiento por selección
===========================================
Fecha: 26 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def seleccion(lista):
    """Ordena una lista de números utilizando el método de selección, mostrando el proceso paso a paso.
    (list) -> None"""
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        
        print(f"Numero enfocado en {lista[i:]}: {lista[min_index]}")
        
        if min_index != i:
            print(f"{lista[i]} <-> {lista[min_index]}")
            lista[i], lista[min_index] = lista[min_index], lista[i]
        else:
            print("Sin intercambios")

        print(lista)

def main():
    entrada = input().strip()
    lista = [int(x) for x in entrada.split()]
    seleccion(lista)

main()
"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Repisa con cajas
===========================================
Fecha: 3 de Diciembre de 2024
Autor: Diego Prado Pardo
===========================================
"""

def leer_datos():
    """ Lee el tamaño de la repisa y su organización inicial.
    () -> int, int, list """
    m, n = map(int, input().split())

    # print(f"Ingrese la organización de las {m} repisas (cada fila debe tener {n} valores):")
    orden = []
    for _ in range(m):
        fila = list(map(int, input().split()))
        orden.append(fila)

    return m, n, orden

def ventarron(m, n, orden):
    """ Simula el efecto del ventarrón sobre las repisas, el cual retorna la organización final.
    (int, int, list) -> list """
    for k in range(m):
        for i in range(n - 2, -1, -1):
            if orden[k][i] == 1:
                j = i
                while j + 1 < n and orden[k][j + 1] == 0:
                    if orden[k][j + 1] == 2:
                        break
                    orden[k][j], orden[k][j + 1] = orden[k][j + 1], orden[k][j]
                    j += 1
    return orden

def imprimir_repisas(repisas):
    """ Imprime la organización de las repisas en formato de matriz.
    (list) -> None """
    for fila in repisas:
        print(" ".join(map(str, fila)))

def main():
    m, n, orden = leer_datos()
    orden_final = ventarron(m, n, orden)
    print("\n")
    imprimir_repisas(orden_final)

main()

"""
5 5

1 0 0 2 0
1 0 1 1 0
2 0 1 0 1
1 0 1 1 0
1 1 1 2 0

0 0 1 2 0
0 0 1 1 1
2 0 0 1 1
0 0 1 1 1
1 1 1 2 0
"""

"""
3 6
1 1 0 0 1 2
1 0 2 0 1 0
2 2 0 0 1 2


0 0 1 1 1 2
0 1 2 0 0 1
2 2 0 0 1 2
"""
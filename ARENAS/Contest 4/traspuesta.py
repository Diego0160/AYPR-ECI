"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 4
Programa: Matriz traspuesta
=========================================
Autor: Diego Prado Pardo
=========================================
"""

def transponer_matriz(matriz, tamano_matriz):
    """Realiza la transposición de una matriz cuadrada en la misma matriz.
    (list, int) -> None"""
    for i in range(tamano_matriz):
        for j in range(i + 1, tamano_matriz):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

def main():
    tamano_matriz = int(input().strip())

    matriz = []
    for _ in range(tamano_matriz):
        fila = list(map(int, input().strip().split(',')))
        matriz.append(fila)

    transponer_matriz(matriz, tamano_matriz)

    for fila in matriz:
        print(",".join(map(str, fila)))

main()
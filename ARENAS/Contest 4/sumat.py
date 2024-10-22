"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 3
Programa: Suma de matrices
=========================================
Autor: Diego Prado Pardo
=========================================
"""
def read_matriz(n, m):
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().replace(',', ' ').split()))
        matriz.append(fila)
    return matriz

def suma_matrices(m1, m2, n, m):
    resultado = []
    for i in range(n):
        a_fila = []
        for j in range(m):
            a_fila.append(m1[i][j] + m2[i][j])
        resultado.append(a_fila)
    return resultado

def print_matriz(matriz):
    for i in range(len(matriz)):
        print(','.join(map(str, matriz[i])))

def main():
    n, m = map(int, input().split(','))
    m1 = read_matriz(n, m)
    input()
    m2 = read_matriz(n, m)
    resultado = suma_matrices(m1, m2, n, m)
    print_matriz(resultado)

main()
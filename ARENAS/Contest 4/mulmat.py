"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 4
Programa: Multiplicación de matrices
=========================================
Autor: Diego Prado Pardo
=========================================
"""
def leer_matriz(filas, columnas):
    """Lee una matriz de tamaño filas x columnas"""
    matrix = []
    for _ in range(filas):
        line = input().strip()
        fila = list(map(int, line.split(',')))
        if len(fila) != columnas:
            raise ValueError("La fila no tiene el número correcto de columnas.")
        matrix.append(fila)
    return matrix

def multiplicar_matrices(A, B):
    """Multiplica dos matrices A y B y devuelve la matriz resultado."""
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    C = [[0] * p for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def print_matriz(matrix):
    """Imprime una matriz en el formato adecuado."""
    for fila in matrix:
        print(','.join(map(str, fila)))

def main():
    m, n = map(int, input().strip().split(','))
    A = leer_matriz(m, n)
    
    n2, p = map(int, input().strip().split(','))
    
    if n != n2:
        print("No es posible")
        return
    
    B = leer_matriz(n2, p)
    result = multiplicar_matrices(A, B)
    print_matriz(result)

main()
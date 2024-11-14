"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Triángulo de Pascal
===========================================
Fecha: 12 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def calcular_siguiente_fila(fila_actual):
    """ Calcula la siguiente fila del triángulo usando la fila actual
    (list) -> list """
    siguiente = [1]
    for i in range(len(fila_actual)-1):
        siguiente.append(fila_actual[i] + fila_actual[i+1])
    siguiente.append(1)
    return siguiente

def generar_triangulo(n):
    """ Genera el triángulo de Pascal hasta el nivel n
    (int) -> list """
    triangulo = [[1]]
    for i in range(n-1):
        siguiente_fila = calcular_siguiente_fila(triangulo[-1])
        triangulo.append(siguiente_fila)
    return triangulo

def main():
    n = int(input())
    
    triangulo = generar_triangulo(n)
    for fila in triangulo:
        print(" ".join(map(str, fila)))

main()
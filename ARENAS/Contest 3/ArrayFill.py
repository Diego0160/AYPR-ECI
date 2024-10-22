"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 3
Programa: Array fill I
=========================================
Autor: Diego Prado Pardo
=========================================
"""
def fill_array(V):
    N = [0] * 10
    for i in range(10):
        N[i] = V
        V *= 2
    return N

def print_array(N):

    for i in range(9):
        print(f"N[{i}] = {N[i]}")

def main():

    V = int(input())
    N = fill_array(V)
    print_array(N)
main()
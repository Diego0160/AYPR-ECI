"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 2
Programa: Relational Operator
=========================================
Autor: Diego Prado Pardo
=========================================
"""
def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        
        if a < b:
            print("<")
        elif a > b:
            print(">")
        else:
            print("=")

main()
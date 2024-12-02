"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Generar lista y archivo datos
===========================================
Fecha: 28 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
import random

def generar_lista(t):
    """ Genera una lista de números aleatorios en el rango de 0 a t * 3.
    (int) -> list """
    lista = [random.randint(0, t * 3) for _ in range(t)]
    return lista

def main():
    t = int(input())
    
    ans = generar_lista(t)
    
    print(",".join(map(str, ans)))

main()

# En consola CMD:
# python genera_arch.py > datos1.in
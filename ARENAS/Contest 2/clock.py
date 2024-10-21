"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 2
Programa: Alarm Clock
=========================================
Autor: Diego Prado Pardo
=========================================
"""
def calcular_minutos(H1, M1, H2, M2):
    minutos_actuales = H1 * 60 + M1
    minutos_alarma = H2 * 60 + M2
    
    if minutos_alarma >= minutos_actuales:
        minutos_sueno = minutos_alarma - minutos_actuales
    else:
        minutos_sueno = (1440 - minutos_actuales) + minutos_alarma
    
    return minutos_sueno

def main():
    H1, M1, H2, M2 = map(int, input().split())
    calcular_minutos(H1, M1, H2, M2)
    
    while H1 != 0 or M1 != 0 or H2 != 0 or M2 != 0:
        print(calcular_minutos(H1, M1, H2, M2))
        H1, M1, H2, M2 = map(int, input().split())

main()
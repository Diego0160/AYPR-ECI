"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Parcial Segundo Tercio
=========================================
Fecha: 24 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def rango(a, b, c, d, m):
    """ Permite verificar si los valores se encuentran en el rango correcto
    (list) -> bool """
    if (a, b, c) >= -100 and (a, b, c) <= 100 and d > 1 and d < 100 and m >= 0 and m < 100:
        return True
    else:
        return False

def cuadratica(a, b, c, d, m):
    
    return None

def main():
    v = input()
    a, b, c, d, m = map(int, v.split(' '))
    rango()
    if rango(a, b, c, d, m) == False or (a, b, c, d, m) == '0 0 0 0 0':
        break
    else:
        cuadratica(a, b, c, d, m)
main()
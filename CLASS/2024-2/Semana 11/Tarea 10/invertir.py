"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Al revés
=========================================
Fecha: 29 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def invertir(input):
    """Función que invierte una secuencia de tipo string.
    (str) -> str"""
    return input[::-1]

def main():
    i = input()
    ans = invertir(i)
    print(ans)

main()
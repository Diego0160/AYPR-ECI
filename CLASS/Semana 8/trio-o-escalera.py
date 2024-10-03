"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Trio o escalera
=========================================
Fecha: 3 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def proceso(sec, sec_i, sec_v):
    """ Función que hace el proceso
    (list, list, list) -> list """
    for i in range(0, len(sec_i)):
        sec[sec_i[i]] = sec_v[i]
    return sec

def main():
    sec = input().split()
    i = 0
    n = len(sec)
    while i < n:
        sec[i] = int(sec[i]) # type: ignore
        i += 1
    #end_while
    sec_i = input().split()
    i = 0
    n = len(sec_i)
    while i < n:
        sec_i[i] = int(sec_i[i]) # type: ignore
        i += 1
    #end_while
    sec_v = input().split()
    i = 0
    n = len(sec_v)
    while i < n:
        sec_v[i] = int(sec_v[i]) # type: ignore
        i += 1
    #end_while
    resultado = proceso(sec, sec_i, sec_v)
    print(resultado)
main()
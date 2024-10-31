"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: 
=========================================
Fecha: 31 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def secuencia_valores(v):
    """ Esta función devuelve una lista con los valores dados por el usuario
    (list) -> list """
    lista = print("Punto 2\n", " ".join(v))
    return lista

def linea(lista):
    """ 
     """
    for v in range(lista):
        ent = print("Punto 3\n", v)
    return ent

def cantidad_e(cantidad):
    """ 
     """
    count = print("Punto 4\n",len(cantidad))
    return count

def main():
    s_lista = []
    v = input()
    s_lista.append(v.split(','))
    print("Punto 1\n", s_lista)
    ans2 = secuencia_valores(v)
    ans3 = linea(v)
    ans4 = cantidad_e(v)
main()
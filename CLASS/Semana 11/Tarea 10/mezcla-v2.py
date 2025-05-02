"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Mezcla
=========================================
Fecha: 31 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def alreves(lista):
    """ Invierte los elementos de una lista
    (list) -> list """
    n = len(lista)
    for i in range(0,n//2):
        aux = lista[i]
        lista[i] = lista[(n-1)-i]
        lista[(n-1)-i] = aux
    return lista

def main():
    datos = input("?").split(",")
    num = int(input("num?"))
    long = len(datos)
    partes = long // num
    mezcla = []
    ini = 0
    fin = partes
    for i in range (num):
        nueva = []
        for j in range(ini, fin):
            nueva.append(datos[j])
        print(nueva)
        ini = fin
        fin += partes 
        mezcla += alreves(nueva)
    print(mezcla)

main()
"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Diagrama de barras
===========================================
Fecha: 12 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def crear_barra(n):
    """ Crea una barra vertical de asteriscos 
    (int) -> str """
    barra = ""
    for i in range(n):
        barra += "* "
    return barra

def dibujar_diagrama(lista):
    """ Dibuja el diagrama de barras con asteriscos usando una lista de números
    (list) -> None """
    maximo = max(lista)
    
    for nivel in range(maximo, 0, -1):
        linea = ""
        for num in lista:
            if num >= nivel:
                linea += "* "
            else:
                linea += "  "
        print(linea)

def main():
    ns = input()
    lista = [int(x) for x in ns.split()]
    
    dibujar_diagrama(lista)

main()
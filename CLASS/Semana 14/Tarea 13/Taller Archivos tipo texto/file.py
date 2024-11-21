"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Taller Archivos tipo texto
===========================================
Fecha: 12 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def lectura(nombre):

    g61 = open('g61.dat', 'r')
    empty_str = ''
    linea = g61.readline()
    while linea != empty_str:
        linea = g61.readline()
    g61.close()
    """char_str = ','
    linea = g61.readline()
    while linea == char_str:
        linea = g61.readline().split(',')
    g61.close() """

def main():
    nombre = input('Ingrese sus nombres y apelidos completo: ').upper()
    email = lectura(nombre)
    print(email)


main()

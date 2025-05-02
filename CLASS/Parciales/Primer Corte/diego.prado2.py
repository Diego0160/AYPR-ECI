"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Parcial Tercio 1
Programa: Conversion de números a nombres
=========================================
Fecha: 19 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def nombre_dia(num):
    """ Entrega el nombre del día se la semana correspondiente al numero dado
    (int) -> str """
    if num == 1 or num == 8 or num == 15 or num == 22 or num == 29:
        num = 'Lunes'
    elif num == 2 or num == 9 or num == 16 or num == 23 or num == 30:
        num = 'Martes'
    elif num == 3 or num == 10 or num == 17 or num == 24 or num == 31:
        num = 'Miercoles'
    elif num == 4 or num == 11 or num == 18 or num == 25:
        num = 'Jueves'
    elif num == 5 or num == 12 or num == 19 or num == 26:
        num = 'Viernes'
    elif num == 6 or num == 13 or num == 20 or num == 27:
        num = 'Sabado'
    elif num == 7 or num == 14 or num == 21 or num == 28:
        num = 'Domingo'
    return str(num)

def main():
    num = int(input('Ingrese un número: '))
    nombre_dia(num)
    print(num)
main()
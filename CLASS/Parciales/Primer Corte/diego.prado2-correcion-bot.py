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
    """ Devuelve el nombre del día de la semana correspondiente al número dado
    (int) -> str """
    dias = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    # El número puede ser más de 7, usamos módulo para obtener el día correcto
    return dias[num % 7]

def main():
    num = int(input('Ingrese un número: '))
    dia = nombre_dia(num)
    print(dia)

main()
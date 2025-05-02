"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Parcial Tercio 1
Programa: Prueba de Conocimiento
=========================================
Fecha: 19 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
from random import randint

def pregunta_1(nota):
    """ Realiza la primera pregunta, obtiene su respuesta y devuelve un resultado
    (float) -> float """
    print('Pregunta 1')
    mes = int(input('Diga mes: '))
    
    if es_mes(mes):
        nota = nota + 2.5
    else:
        nota += 0
        
    return pregunta_2(nota)

def pregunta_2(nota):
    """ Realiza la segunda pregunta, obtiene su respuesta y devuelve un resultado
    (float, int, int) -> float """
    print('Pregunta 2')
    rnum = randint(1, 99)
    num = int(input(f'El número menor que {rnum} es: '))
    
    unidades, decenas = uni_dec(num, rnum)
    print(f'Unidades: {unidades}')
    print(f'Decenas: {decenas}')
    
    if unidades is not None:
        nota = nota + 2.5
    elif nota == 0.0:
        nota = nota + 1.0
    
    return nota

def es_mes(mes):
    """ Dice si un número del mes es válido
    (int) -> bool """
    return 1 <= mes <= 12

def uni_dec(num, rnum):
    """ Entrega unidades y decenas de un número menor que 100
    (int) -> int, int """
    if num < rnum:
        unidades = num % 10
        decenas = num // 10
        return unidades, decenas
    return None, None

def main():
    name = input('Diga su Nombre: ')
    nota = pregunta_1(0.0)

    if 2.0 < nota < 3.0:
        mensaje = 'y puede mejorar'
    elif nota < 2.0:
        mensaje = 'y debe citar a supletorio'
    else:
        mensaje = 'felicidades'

    print(f'{name} su nota es: {nota} {mensaje}')

main()
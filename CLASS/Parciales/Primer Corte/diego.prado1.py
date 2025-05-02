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
    es_mes(mes)

    if mes == True:
        print ('si')
        nota = nota + 2.5
        return nota
    elif mes == False:
        print('no')
        return nota

    return pregunta_2(nota)

def pregunta_2(nota):
    """ Realiza la segunda pregunta, obtiene su respuesta y devuelve un resultado
    (float, int, int) -> float """
    #print(nota) -- Verificación de nota actual
    print('Pregunta 2')
    u = 0
    d = 0
    rnum = randint(1, 99)
    num = int(input(f'El número menor que {rnum} es: '))
    uni_dec(num, rnum, u, d)
    print(f'Unidades: {u}')
    print(f'Decenas: {d}')
    if num == True:
        nota = nota + 2.5
    elif uni_dec == False and nota == 0.0:
        nota = nota + 1.0
    elif uni_dec == False and nota > 0.0:
        nota
    return nota

def es_mes(mes):
    """ Dice si un número del mes es válido
    (int) -> bool """
    if mes >= 1 and mes <= 12:
        mes = True
    else:
        mes = False
    return mes

def uni_dec(num, rnum, u, d):
    """ Entrega unidades y decenas de un número menor que 100
    (int) -> int, int """
    if num < rnum:
        u = (num % 10)
        return u
    elif num < rnum:
        d = (num % 1)
        return d
    elif num < rnum:
        num = True
        return num
    else:
        return False

def main():
    name = input('Diga su Nombre: ')
    nota = pregunta_1(0.0)

    if nota < 3.0 and nota > 2.0:
        mensaje = 'y puede mejorar'
    elif nota < 2.0:
        mensaje = 'y debe citar a supletorio'
    else:
        mensaje = 'felicidades'

    print(f'{name} su nota es: {nota} {mensaje}')
main()

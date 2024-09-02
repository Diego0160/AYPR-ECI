"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
SubPrograma: Librerias de dibujo de 
             Figuras
=========================================
Fecha: 29 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
#LIBRERIAS
import turtle
import lib_areas_y_perimetros
lapiz = turtle.Turtle()
l = lapiz
l.speed(2)
l.pensize(5)

def dibujo_triangulo(base, altura):
    ''' 

    '''
    l.pu()
    l.goto(-base/2, -altura/2)
    l.pd()
    l.begin_fill()
    l.color("blue")
    l.forward(10 * base)
    l.left(90)
    l.forward(10 * altura)
    l.left(90)
    l.goto(-base/2, -altura/2)
    l.end_fill()
    l.hideturtle()

def dibujo_rectangulo(base, altura):
    ''' 

    '''
    l.pu()
    l.goto(-base/2, -altura/2)
    l.pd()
    l.begin_fill()
    l.color("green")
    l.forward(base)
    l.left(90)
    l.forward(altura)
    l.left(90)
    l.forward(base)
    l.left(90)
    l.forward(altura)
    l.left(90)
    l.end_fill()
    l.hideturtle()

def dibujo_trapecio(base_mayor, base_menor, altura):
    ''' 

    '''
    l.pu()
    l.goto(-base_mayor/2, 0)
    l.pd()
    l.begin_fill()
    l.color("orange")
    l.forward(10 * base_mayor)
    l.left(135)
    l.forward(10 * ((((base_mayor - base_menor) / 2) ** 2 + altura ** 2) ** 0.5))
    l.left(45)
    l.forward(10 * base_menor)
    l.left(45)
    l.forward(10 * ((((base_mayor - base_menor) / 2) ** 2 + altura ** 2) ** 0.5))
    l.goto(-base_mayor/2, 0)
    l.end_fill()
    l.hideturtle()

def dibujo_estrella(longitud):
    ''' 

    '''
    l.pu()
    l.goto(-longitud/2, 0)
    l.pd()
    l.begin_fill()
    l.color("yellow")
    l.forward(10 * longitud)
    l.right(144)
    l.forward(10 * longitud)
    l.right(144)
    l.forward(10 * longitud)
    l.right(144)
    l.forward(10 * longitud)
    l.right(144)
    l.forward(10 * longitud)
    l.goto(-longitud/2, 0)
    l.end_fill()
    l.hideturtle()
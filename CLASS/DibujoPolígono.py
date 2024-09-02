"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa Polígono
=========================================
Fecha: 15 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
import turtle
lapiz = turtle.Turtle()
l = lapiz
l.filling()
l.begin_fill()
l.speed(10)
l.pensize(5)
l.pu()
l.goto(-1,1)
l.pd()
radio = input("Digite el valor de radio que usted desee: ")
radio = int(radio)
area_c=3.14*radio**2
l.back(area_c)
l.right(-90)
l.forward(area_c)
l.right(90)
l.forward(area_c)
l.left(90)
l.back(area_c)
l.color("Yellow")
l.end_fill()
print("El área del polinómio es:", area_c)


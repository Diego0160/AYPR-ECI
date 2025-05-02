"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Dibujo Robot
=========================================
Fecha: 15 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
import turtle

# Nombramos un Identificador llamado lapiz, el cuál se le define el comando turtle.Turtle()
lapiz = turtle.Turtle()
# Asignaremos la letra l al Identificador lapiz para agilizar la escritura del código.
l = lapiz
# Se asigna una velocidad al programa para agilizar el proceso de trazado
l.speed(10)
# Se asigna el tamaño del lápiz para dibujo
l.pensize(5)

# Dibujamos el primer cuadrado con el color azul
l.left(20)
l.color("blue")
l.begin_fill()

l.forward(100)
l.left(90)
l.forward(100)
l.left(90)
l.forward(100)
l.left(90)
l.forward(100)
l.left(90)

l.end_fill()

# Dibujamos el segundo cuadrado con el color amarillo
l.left(20)
l.color("yellow")
l.begin_fill()

l.forward(100)
l.left(90)
l.forward(100)
l.left(90)
l.forward(100)
l.left(90)
l.forward(100)
l.left(90)

l.end_fill()

# Dibujamos el tercer cuadrado con el color rojo
l.left(20)
l.color("red")
l.begin_fill()

l.forward(100)
l.left(90)
l.forward(100)
l.left(90)
l.forward(100)
l.left(90)
l.forward(100)
l.left(90)

l.end_fill()

# Ocultamos el lapiz
l.hideturtle()

# Para evitar que la ventana se cierre, utilizaremos turtle.done() para indicar que el programa ha terminado su dibujo y este mantenga la ventana abierta.
turtle.done()
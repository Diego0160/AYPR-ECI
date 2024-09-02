"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa Triángulo
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

# Solicitar la base y altura del triángulo al usuario
base = input("Digite el valor de la base del triángulo: ")
altura = input("Digite el valor de la altura del triángulo: ")

# Para evitar errores en el código, definiremos los valores de la base y la altura como números enteros
base = int(base)
altura = int(altura)

# Calcular el área, el perímetro y la hipotenusa con los valores anteriores
hipotenusa = (base ** 2 + altura ** 2) ** 0.5
area = (base * altura) / 2
perimetro = base + altura + hipotenusa

# Centramos el triángulo para realizar su dibujo
l.pu()
l.goto(-base/2, -altura/2)
l.pd()
l.begin_fill()
l.color("blue")
l.forward(base)
l.left(90)
l.forward(altura)
l.left(90)
l.goto(-base/2, -altura/2)
l.end_fill()

# Mostrar los cálculos realizados
print(f"El área del triángulo es: {area}")
print(f"El perímetro del triángulo es: {perimetro}")
print(f"La longitud de la hipotenusa es: {hipotenusa}")

# Ocultamos el lapiz
l.hideturtle()

# Para evitar que la ventana se cierre, utilizaremos turtle.done() para indicar que el programa ha terminado su dibujo y este mantenga la ventana abierta.
turtle.done()
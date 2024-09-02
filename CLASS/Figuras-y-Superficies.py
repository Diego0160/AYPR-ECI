"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Figuras y Superficies
=========================================
Fecha: 26 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
import turtle
from math import pi

# Nombramos un Identificador llamado lapiz, el cuál se le define el comando turtle.Turtle()
lapiz = turtle.Turtle()
# Asignamos la letra l al Identificador lapiz para agilizar la escritura del código.
l = lapiz
# Se asigna una velocidad al programa para verificar el proceso de trazado
l.speed(2)
# Se asigna el tamaño del lápiz para dibujo
l.pensize(5)

figura = input('Escriba la figura que desee (triangulo, rectangulo, trapecio, estrella): ').lower()
condicion = input('¿Desea calcular area (a) o perimetro (p)? ').lower()

if (figura == 'triangulo' or figura == 'triángulo' or 
    figura == 'rectangulo' or figura == 'rectángulo' or 
    figura == 'trapecio' or figura == 'estrella'):
    
    if condicion == 'a' or condicion == 'p':
        
        if figura == 'triangulo' or figura == 'triángulo':
            base = int(input("Digite el valor de la base del triángulo: "))
            altura = int(input("Digite el valor de la altura del triángulo: "))

            if condicion == 'a':
                area = (base * altura) / 2
            elif condicion == 'p':
                hipotenusa = (base ** 2 + altura ** 2) ** 0.5
                perimetro = base + altura + hipotenusa

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

        elif figura == 'rectangulo' or figura == 'rectángulo':
            base = int(input("Digite el valor de la base del rectángulo: "))
            altura = int(input("Digite el valor de la altura del rectángulo: "))

            if condicion == 'a':
                area = base * altura
            elif condicion == 'p':
                perimetro = 2 * (base + altura)

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

        elif figura == 'trapecio':
            base_mayor = int(input("Digite el valor de la base mayor del trapecio: "))
            base_menor = int(input("Digite el valor de la base menor del trapecio: "))
            altura = int(input("Digite el valor de la altura del trapecio: "))

            if condicion == 'a':
                area = (base_mayor + base_menor) * altura / 2
            elif condicion == 'p':
                lado_oblicuo = (((base_mayor - base_menor) / 2) ** 2 + altura ** 2) ** 0.5
                perimetro = base_mayor + base_menor + 2 * lado_oblicuo

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

        elif figura == 'estrella':
            longitud = int(input("Digite la longitud de los lados de la estrella: "))

            if condicion == 'a':
                area = (5 / 4) * (longitud ** 2) * (1 + (2 * (5 ** 0.5)))
            elif condicion == 'p':
                perimetro = 10 * longitud

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

    else:
        print('Error: No se ha especificado si desea calcular área (a) o perímetro (p)')
        exit()

else:
    print('Error: No ha especificado una figura válida (triangulo, rectangulo, trapecio, estrella)')
    exit()

# Mostrar los cálculos realizados
if condicion == 'a':
    if figura == 'triangulo' or figura == 'triángulo' or figura == 'rectangulo' or figura == 'rectángulo' or figura == 'trapecio' or figura == 'estrella':
        print(f"El área del {figura} es: {round(area, 2)}")
elif condicion == 'p':
    if figura == 'triangulo' or figura == 'triángulo' or figura == 'rectangulo' or figura == 'rectángulo' or figura == 'trapecio' or figura == 'estrella':
        print(f"El perímetro del {figura} es: {round(perimetro, 2)}")

# Ocultamos el lápiz
l.hideturtle()

# Para evitar que la ventana se cierre, utilizamos turtle.done() para indicar que el programa ha terminado su dibujo y este mantenga la ventana abierta.
turtle.done()
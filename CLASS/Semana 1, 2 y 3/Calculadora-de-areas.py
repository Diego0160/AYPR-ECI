"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Calculadora de Áreas
=========================================
Fecha: 21 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
from math import pi

entrada = input('Escribe la figura que desees (triángulo, rectángulo, círculo, cuadrado): ')

if entrada == 'triángulo' or entrada == 'triangulo' or entrada == 'Triángulo' or entrada == 'Triangulo' or entrada == 'rectángulo' or entrada == 'rectangulo' or entrada == 'Rectángulo' or entrada == 'Rectangulo':
    base = float(input('Ingresa la base de la figura: '))
    altura = float(input('Ingresa la altura de la figura: '))
elif entrada == 'círculo' or entrada == 'circulo' or entrada == 'Círculo' or entrada == 'Circulo':
    radio = float(input('Ingresa el radio de la figura: '))
elif entrada == 'cuadrado' or entrada == 'Cuadrado':
    lado = float(input('Ingresa el lado de la figura: '))
else:
    print('Error')
    exit()

if entrada == 'triángulo' or entrada == 'triangulo' or entrada == 'Triángulo' or entrada == 'Triangulo':
    area_triangulo = (base * altura) / 2
    print(f'El área del {entrada} es: {round(area_triangulo, 2)}')
elif entrada == 'rectángulo' or entrada == 'rectangulo' or entrada == 'Rectángulo' or entrada == 'Rectangulo':
    area_rectangulo = base * altura
    print(f'El área del {entrada} es: {round(area_rectangulo, 2)}')
elif entrada == 'círculo' or entrada == 'circulo' or entrada == 'Círculo' or entrada == 'Circulo':
    area_circulo = pi * radio ** 2
    print(f'El área del {entrada} es: {round(area_circulo, 2)}')
elif entrada == 'cuadrado' or entrada == 'Cuadrado':
    area_cuadrado = lado ** 2
    print(f'El área del {entrada} es: {round(area_cuadrado, 2)}')

"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Rectangulo
=========================================
Fecha: 24 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def dibujar_rectangulo(altura, ancho, caracter):
    """ Dibuja un rectángulo con las dimensiones y el carácter proporcionado.
    (int, int, str) -> None """
    n = 0
    while n < altura:
        print(caracter * ancho)
        n += 1

def main():
    altura = int(input("Ingresa la altura del rectángulo: "))
    ancho = int(input("Ingresa el ancho del rectángulo: "))
    caracter = input("Ingresa un carácter: ")
    
    dibujar_rectangulo(altura, ancho, caracter)
main()


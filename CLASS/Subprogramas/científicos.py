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
import lib_areas_y_perimetros as layp
import lib_figuras as figuras

def main():
    figura = input('Escriba la figura que desee (triangulo, rectangulo, trapecio, estrella): ').lower()
    condicion = input('¿Desea calcular área (a) o perimetro (p)? ').lower()

    if (figura == 'triangulo' or figura == 'triángulo' or 
        figura == 'rectangulo' or figura == 'rectángulo' or 
        figura == 'trapecio' or figura == 'estrella'):
        
        if condicion == 'a' or condicion == 'p':
            
            if figura == 'triangulo' or figura == 'triángulo':
                base = int(input("Digite el valor de la base del triángulo: "))
                altura = int(input("Digite el valor de la altura del triángulo: "))
                if condicion == 'a':
                    area = layp.area_triangulo(base, altura)
                else:
                    perimetro = layp.perimetro_triangulo(base, altura)
                figuras.dibujo_triangulo(base, altura)

            elif figura == 'rectangulo' or figura == 'rectángulo':
                base = int(input("Digite el valor de la base del rectángulo: "))
                altura = int(input("Digite el valor de la altura del rectángulo: "))
                if condicion == 'a':
                    area = layp.area_rectangulo(base, altura)
                else:
                    perimetro = layp.perimetro_rectangulo(base, altura)
                figuras.dibujo_rectangulo(base, altura)

            elif figura == 'trapecio':
                base_mayor = int(input("Digite el valor de la base mayor del trapecio: "))
                base_menor = int(input("Digite el valor de la base menor del trapecio: "))
                altura = int(input("Digite el valor de la altura del trapecio: "))
                if condicion == 'a':
                    area = layp.area_trapecio(base_mayor, base_menor, altura)
                else:
                    perimetro = layp.perimetro_trapecio(base_mayor, base_menor, altura)
                figuras.dibujo_trapecio(base_mayor, base_menor, altura)

            elif figura == 'estrella':
                longitud = int(input("Digite la longitud de los lados de la estrella: "))
                if condicion == 'a':
                    area = layp.area_estrella(longitud)
                else:
                    perimetro = layp.perimetro_estrella(longitud)
                figuras.dibujo_estrella(longitud)

            # Mostrar los cálculos realizados
            if condicion == 'a':
                print(f"El área del {figura} es: {round(area, 2)}")
            elif condicion == 'p':
                print(f"El perímetro del {figura} es: {round(perimetro, 2)}")

        else:
            print('Error: No se ha especificado si desea calcular área (a) o perímetro (p)')
            exit()

    else:
        print('Error: No ha especificado una figura válida (triangulo, rectangulo, trapecio, estrella)')
        exit()

    turtle.done()
main()
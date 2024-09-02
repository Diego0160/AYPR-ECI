"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
SubPrograma: Librerias de áreas y  
             Perímetros
=========================================
Fecha: 29 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
#LIBRERIAS
def area_triangulo(base, altura):
    ''' 
    CALCULA EL ÁREA DE UN TRIANGULO POR MEDIO DE BASE Y ALTURA
    '''
    area = (base * altura) / 2
    return area

def perimetro_triangulo(base, altura):
    ''' 
    CALCULA EL PERIMETRO DE UN TRIANGULO POR MEDIO DE BASE Y ALTURA
    '''
    hipotenusa = (base ** 2 + altura ** 2) ** 0.5
    perimetro = base + altura + hipotenusa
    return perimetro

def area_rectangulo(base, altura):
    ''' 
    CALCULA EL ÁREA DE UN RECTANGULO POR MEDIO DE BASE Y ALTURA
    '''
    area = base * altura
    return area

def perimetro_rectangulo(base, altura):
    ''' 
    CALCULA EL PERIMETRO DE UN RECTANGULO POR MEDIO DE BASE Y ALTURA
    '''
    perimetro = 2 * (base + altura)
    return perimetro

def area_trapecio(base_mayor, base_menor, altura):
    ''' 
    CALCULA EL ÁREA DE UN TRAPECIO POR MEDIO DE SU BASE MAYOR, BASE MENOR Y ALTURA
    '''
    area = (base_mayor + base_menor) * altura / 2
    return area

def perimetro_trapecio(base_mayor, base_menor, altura):
    ''' 
    CALCULA EL PERIMETRO DE UN TRAPECIO POR MEDIO DE SU BASE MAYOR, BASE MENOR Y ALTURA
    '''
    lado_oblicuo = (((base_mayor - base_menor) / 2) ** 2 + altura ** 2) ** 0.5
    perimetro = base_mayor + base_menor + 2 * lado_oblicuo
    return perimetro

def area_estrella(longitud):
    ''' 
    CALCULA EL ÁREA DE LA ESTRELLA POR MEDIO DE LA LONGITUD (lados de la estrella)
    '''
    area = (5 / 4) * (longitud ** 2) * (1 + (2 * (5 ** 0.5)))
    return area

def perimetro_estrella(longitud):
    ''' 
    CALCULA EL PERIMETRO DE LA ESTRELLA POR MEDIO DE LA LONGITUD (lados de la estrella)
    '''
    perimetro = 10 * longitud
    return perimetro
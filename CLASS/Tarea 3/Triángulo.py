"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Verificación de Triángulos
=========================================
Fecha: 3 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
lnv = 'Longitud no Válida'

def valido_tri(a, b, c):
    """ Verifica que si con tres longitudes se puede armar un triángulo
    (int, int, int) -> bool """
    if a <= 0 or b <= 0 or c <= 0:
        return lnv
    
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def tipo_tri(a, b, c):
    """ Verifica qué tipo de triángulo es según sus lados
    (int, int, int) -> str """
    if a == b == c:
        return 'Equilatero'
    elif a == b or a == c or b == c:
        return 'Isósceles'
    else:
        return 'Escaleno'

def main():
    a = int(input('Digite la longitud del primer lado: '))
    b = int(input('Digite la longitud del segundo lado: '))
    c = int(input('Digite la longitud del tercer lado: '))

    t_valido = valido_tri(a, b, c)
    
    if t_valido == True:
        t_tipo = tipo_tri(a, b, c)
        print (f'El triangulo es {t_tipo}')
    elif t_valido == lnv:
        print (t_valido)
    else:
        print ('No es posible armar un triángulo')

main()
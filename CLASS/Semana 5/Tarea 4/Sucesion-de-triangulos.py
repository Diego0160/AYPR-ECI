"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Sucesion de Triangulos
=========================================
Fecha: 10 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def leer_entero():
    """Valida que el valor ingresado sea un entero,
    () -> int"""
    try:
        valor = int(input("Digite un valor entero: "))
        return valor
    except:
        return -1

def leer_caracter():
    """Solicita un carácter al usuario,
    () -> str"""
    caracter = input("Digite un carácter para formar los triángulos: ")
    if len(caracter) == 1:
        return caracter
    else:
        return None

def imprimir_triangulo(n, caracter):
    """Imprime un triángulo con 'n' líneas usando el carácter dado,
    (int, str) -> None"""
    if n > 0:
        imprimir_triangulo(n - 1, caracter)
        print(caracter * n)

def imprimir_sucesion(n, caracter):
    """Imprime una sucesión de 'n' triángulos usando el carácter dado,
    (int, str) -> None"""
    if n > 0:
        imprimir_triangulo(n, caracter)
        print()
        imprimir_sucesion(n - 1, caracter)

def main():
    valor = leer_entero()
    if valor != -1:
        caracter = leer_caracter()
        if caracter is not None:
            imprimir_sucesion(valor, caracter)
        else:
            print("No ingresaste un carácter válido.")
    else:
        print("El valor ingresado no es un entero válido.")

main()
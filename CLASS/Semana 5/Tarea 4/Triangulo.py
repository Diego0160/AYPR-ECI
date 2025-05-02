"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Triangulo
=========================================
Fecha: 10 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def leer_entero():
    """Valida que el valor ingresado sea un entero, 
    () -> int"""
    valor = input("Digite un valor entero: ")
    
    try: 
        valor = int(valor)
        return valor
    except:
        return -1

def valor_absoluto(valor):
    """Devuelve el valor absoluto de un número,
    (int) -> int"""
    return abs(valor)

def imprimir_triangulo(n):
    """Imprime un triángulo de forma recursiva,
    (int) -> None"""
    if n > 0:
        print('*' * n)
        imprimir_triangulo(n - 1)

def main():
    valor = leer_entero()
    if valor != -1:
        valor = valor_absoluto(valor)
        if valor == 0:
            print(":(")
        else:
            imprimir_triangulo(valor)
    else:
        print("El valor ingresado no es un entero válido")

main()
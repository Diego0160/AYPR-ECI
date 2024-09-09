"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: La calculadora
=========================================
Fecha: 5 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def leer_valor():
    """ Nos permite ingresar datos
    ( ) -> int """
    return int(input("Digite un valor: "))

def suma(a, b):
    """ Realiza la operación suma
    (int, int) -> int """
    return a + b

def resta(a, b):
    """ Realiza la operación resta
    (int, int) -> int """
    return a - b

def producto(a, b):
    """ Realiza la operación multiplicación
    (int, int) -> int """
    return a * b

def divreal(a, b):
    """ Realiza la operación división
    (int, int) -> float """
    if b == 0:
        """ Comprueba si el valor es cero """
        return "No se puede dividir por cero."
    return a / b

def potencia(a, b):
    """ Realiza la operación potencia
    (int, int) -> int """
    return a ** b

def imprimir_valor(valor):
    """ Permite imprimir un valor
    (int o float) -> None """
    print("El resultado es:", valor)

def main():
    try:
        num1 = leer_valor("Digite el valor de num1: ")
        num2 = leer_valor("Digite el valor de num2: ")
        operador = input("Digite operador (+, -, *, /, **): ")

        operaciones = {
            "+": suma,
            "-": resta,
            "*": producto,
            "/": divreal,
            "**": potencia
        }

        if operador in operaciones:
            if operador == "/" and num2 == 0:
                resp = "No se puede dividir por cero."
            else:
                resp = operaciones[operador](num1, num2)
        else:
            resp = "Error: operación no válida"

        imprimir_valor(resp)

    except ValueError:
        print("Por favor, ingresa un número válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

main()

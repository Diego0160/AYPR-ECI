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
    num1 = leer_valor()
    num2 = leer_valor()
    operador = input("Digite que operación desea realizar (+, -, *, /, **): ")
    
    if operador == "+":
        resp = suma(num1, num2)
    elif operador == "-":
        resp = resta(num1, num2)
    elif operador == "*":
        resp = producto(num1, num2)
    elif operador == "/":
        if num2 != 0:
            resp = divreal(num1, num2)
        else:
            resp = "No se puede dividir por cero."
    elif operador == "**":
        resp = potencia(num1, num2)
    else:
        resp = "Error: operación no válida"
    
    imprimir_valor(resp)

main()

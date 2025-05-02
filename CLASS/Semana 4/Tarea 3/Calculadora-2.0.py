"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Calculadora
=========================================
Fecha: 3 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""

def div_entera(a, b):
    if b == 0:
        return "No se puede dividir por cero."
    return a // b

def modulo(a, b):
    if b == 0:
        return "No se puede dividir por cero."
    return a % b

def div_real(a, b):
    if b == 0:
        return "No se puede dividir por cero."
    return a / b

def entradass(entrada, a, b):
    if entrada == "1":
        resultado = div_entera(a, b)
        print("División entera: ", resultado)
    elif entrada == "2":
        resultado = modulo(a, b)
        print("Módulo: ", resultado)
    elif entrada == "3":
        resultado = div_real(a, b)
        print("División real: ", resultado)
    else:
        print("Entrada inválida")

def main():
    entrada = input("Digita 1 para división entera (//) \nDigita 2 para módulo (%)\nDigita 3 para división real (/)\n")
    try:
        a = int(input("Digite el valor de a: "))
        b = int(input("Digite el valor de b: "))    
        entradass(entrada, a, b)
    except ValueError:
        print("Por favor, ingresa un número válido.")

main()
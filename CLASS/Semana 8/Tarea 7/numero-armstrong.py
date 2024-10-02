"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Numero de Armstrong
=========================================
Fecha: 1 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def es_numero_armstrong(n):
    numero_original = n
    numero_digitos = len(str(n))
    suma = 0

    primer_digito = True

    while n > 0:
        digito = n % 10
        n = n // 10
        valor = digito ** numero_digitos
        suma += valor

        if primer_digito:
            print(str(digito) + "^" + str(numero_digitos), end="")
            primer_digito = False
        else:
            print(" + " + str(digito) + "^" + str(numero_digitos), end="")

    print(" = " + str(suma))

    if suma == numero_original:
        print(str(numero_original) + " es un número de Armstrong")
    else:
        print(str(numero_original) + " no es un número de Armstrong")

def main():
    num = int(input(""))
    es_numero_armstrong(num)

main()
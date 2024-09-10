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
# Extra: Se importa random para el uso de una funcion que obtenga una frase cada vez que se solicite
def leer_entero():
    """Valida que el valor ingresado sea un entero, 
    () -> int"""
    valor = input("Digite un valor entero: ")
    
    try: 
        valor = int(valor)
        return valor
    except:
        return -1

def valor_absoluto():
    """ Devuelve el valor absoluto de un numero
    (int) -> int
    """
    return abs(valor)
import random

def main():

    notas = input("Ingrese tres notas separadas por espacio: ")
    
    nota1, nota2, nota3 = map(float, notas.split())
    
    nota_promedio = promedio(nota1, nota2, nota3)
    
    if nota_promedio >= 4.5:
        print("¡Felicidades! Obtuvo una nota superior.")
    elif nota1 >= 4.5 or nota2 >= 4.5 or nota3 >= 4.5:
        print(mensaje_motivador())
    else:
        print()

main()
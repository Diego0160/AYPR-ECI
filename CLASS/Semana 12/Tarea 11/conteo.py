"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Conteo
===========================================
Fecha: 5 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""

def contar_cantidad(cadena):
    """ Cuenta la cantidad de vocales, consonantes y espacios en una cadena de texto.
    (str) -> int,int,int """
    
    vocales = 0
    consonantes = 0
    espacios = 0
    letras_vocales = "AEIOUaeiou"  
    
    for caracter in cadena:
        if caracter in letras_vocales:
            vocales += 1
        elif caracter.isalpha():
            consonantes += 1
        elif caracter.isspace():
            espacios += 1
    
    return vocales, consonantes, espacios

def main():
    cadena = input()
    vocales, consonantes, espacios = contar_cantidad(cadena)
    print("Vocales:", vocales)
    print("Consonantes:", consonantes)
    print("Espacios:", espacios)

main()

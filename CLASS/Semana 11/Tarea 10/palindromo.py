"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Palíndromo
=========================================
Fecha: 29 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def es_palindromo(cadena):
    """Verifica si una cadena de caracteres es un palíndromo.
    (str) -> bool"""
    cadena = cadena.lower()
    palindromo = cadena[::-1]
    return cadena == palindromo

def main():
    cadena = input()
    if es_palindromo(cadena):
        print("Es palindromo")
    else:
        print("No es palindromo")

main()
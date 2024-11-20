"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 5
Programa: Cifrado César
=========================================
Autor: Diego Prado Pardo
=========================================
"""

def cifrar_cadena(texto, k):
    """ Cifra una cadena desplazando solo las letras k posiciones 
    (str, int) -> str """
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = 65 if caracter.isupper() else 97
            nuevo_cod = (ord(caracter) - base + k) % 26
            resultado += chr(nuevo_cod + base)
        else:
            resultado += caracter
    return resultado

def main():
    n = int(input())
    
    for i in range(n):
        texto = input()
        k = int(input())
        resultado = cifrar_cadena(texto, k)
        print(f"Case{i+1} = {resultado}")

main()
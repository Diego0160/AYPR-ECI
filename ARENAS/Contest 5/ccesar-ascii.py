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
        # Solo cifrar letras, mantener otros caracteres igual
        if caracter.isalpha():
            # Determinar el código ASCII base (65 para mayúsculas, 97 para minúsculas)
            base = 65 if caracter.isupper() else 97
            # Convertir a número (0-25), aplicar desplazamiento y volver a letra
            nuevo_cod = (ord(caracter) - base + k) % 26
            resultado += chr(nuevo_cod + base)
        else:
            resultado += caracter
    return resultado

def main():
    # Leer número de casos
    n = int(input())
    
    # Procesar cada caso
    for i in range(n):
        texto = input()
        k = int(input())
        resultado = cifrar_cadena(texto, k)
        print(f"Case{i+1} = {resultado}")

if __name__ == "__main__":
    main()
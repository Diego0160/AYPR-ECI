"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Test # 17: El mensaje secreto
===========================================
Fecha: 7 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def cifrar_mensaje(mensaje):
    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valores = [1, 2, 9, 3, 4, 10, 5, 11, 12, 13, 14, 15, 16, 17, 18, 6, 7, 8, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    
    palabras = mensaje.lower().split()
    mensaje_cifrado = []
    
    for palabra in palabras:
        palabra_cifrada = []
        for letra in palabra:
            if letra in lista_letras:
                index = lista_letras.index(letra)
                palabra_cifrada.append(str(valores[index]))
        
        mensaje_cifrado.append('_'.join(palabra_cifrada))
    
    return ' '.join(mensaje_cifrado)

def main():
    mensaje = input()
    mensaje_cifrado = cifrar_mensaje(mensaje)
    print(mensaje_cifrado)

main()
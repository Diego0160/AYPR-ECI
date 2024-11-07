"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Problema: El mensaje secreto
===========================================
Fecha: 6 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def cifrar_mensaje(mensaje):
    mapeo = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 4, 'f': 6, 'g': 7, 'h': 8, 
        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 17, 'ñ': 14, 
        'o': 15, 'p': 16, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 
        'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27
    }
    
    palabras = mensaje.lower().split()
    mensaje_cifrado = []
    
    for palabra in palabras:
        palabra_cifrada = []
        for letra in palabra:
            if letra in mapeo:
                palabra_cifrada.append(str(mapeo[letra]))
        
        if palabra_cifrada:
            mensaje_cifrado.append('_'.join(palabra_cifrada))
    
    return ' '.join(mensaje_cifrado)

def descifrar_mensaje(mensaje_cifrado):
    mapeo_inverso = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'e', '6': 'f', '7': 'g', 
        '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', 
        '14': 'ñ', '15': 'o', '16': 'p', '17': 'n', '18': 'q', '19': 'r', 
        '20': 's', '21': 't', '22': 'u', '23': 'v', '24': 'w', '25': 'x', 
        '26': 'y', '27': 'z'
    }
    
    palabras_cifradas = mensaje_cifrado.split()
    mensaje_descifrado = []
    
    for palabra_cifrada in palabras_cifradas:
        letras = []
        numeros = palabra_cifrada.split('_')
        
        for numero in numeros:
            if numero in mapeo_inverso:
                letras.append(mapeo_inverso[numero])
                
        mensaje_descifrado.append(''.join(letras))
    
    return ' '.join(mensaje_descifrado)

def main():
    mensaje = input('Ingrese el mensaje a cifrar: ')
    mensaje_cifrado = cifrar_mensaje(mensaje)
    print('Mensaje cifrado:', mensaje_cifrado)
    
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)
    print('Mensaje descifrado:', mensaje_descifrado)

main()
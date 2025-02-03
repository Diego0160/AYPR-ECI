"""
============================================================
AYPR-アルゴリズムとプログラミング
グループ61
Try#17:秘密のメッセージ
============================================================
日付:2024年11月7日
作者:Diego Prado Pardo
============================================================
"""
def cifrar_mensaje(mensaje: str) -> str:
    letras_a_numeros = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valores = [1, 2, 9, 3, 4, 10, 5, 11, 12, 13, 14, 15, 16, 17, 18, 6, 7, 8, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    
    palabras = mensaje.lower().split()
    mensaje_cifrado = []
    
    for palabra in palabras:
        palabra_cifrada = []
        for letra in palabra:
            if letra in letras_a_numeros:
                index = letras_a_numeros.index(letra)
                palabra_cifrada.append(str(valores[index]))
        
        mensaje_cifrado.append('_'.join(palabra_cifrada))
    
    return ' '.join(mensaje_cifrado)

def descifrar_mensaje(mensaje_cifrado: str) -> str:
    letras_a_numeros = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valores = [1, 2, 9, 3, 4, 10, 5, 11, 12, 13, 14, 15, 16, 17, 18, 6, 7, 8, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    
    palabras_cifradas = mensaje_cifrado.split()
    mensaje_descifrado = []
    
    for palabra_cifrada in palabras_cifradas:
        letras = []
        numeros = palabra_cifrada.split('_')
        
        for numero in numeros:
            num = int(numero)
            if num in valores:
                index = valores.index(num)
                letras.append(letras_a_numeros[index])
                
        mensaje_descifrado.append(''.join(letras))
    
    return ' '.join(mensaje_descifrado)

def main() -> None:
    mensaje = input('Ingrese el mensaje a cifrar: ')
    mensaje_cifrado = cifrar_mensaje(mensaje)
    print('Mensaje cifrado:', mensaje_cifrado)
    
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)
    print('Mensaje descifrado:', mensaje_descifrado)

main()
"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Cuerdas vocales
===========================================
Fecha: 5 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def reemplazo (frase, vocal):
    '''Reemplaza las vocales de la frase por una vocal
    (str) -> str'''
    vocales = 'aeiouAEIOU'
    nueva_frase = ''
    for letra in frase:
        if letra in vocales:
            nueva_frase += vocal.upper() if letra.isupper() else vocal
        else:
            nueva_frase += letra
    return nueva_frase

def main():
    frase = input()
    vocales = 'aeiou'

    for vocal in vocales:
        f_reemplazo = reemplazo(frase, vocal)
        print(f'Con {vocal}: {f_reemplazo}')
    
main()

"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Códigos
===========================================
Fecha: 19 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def codificar_palabra(palabra):
    """ Codifica una palabra siguiendo las reglas dadas.
    (str) -> str """
   
    vocales = 'aeiou'
    palabra_codificada = ''
    vocales_pos = []
    
    for letra in palabra:
        if letra.lower() in vocales:
            vocales_pos.append(len(palabra_codificada))
            palabra_codificada += letra
        else:
            palabra_codificada += letra
    
    contador = 1
    for pos in vocales_pos:
        palabra_codificada = (palabra_codificada[:pos + contador] +
                            str(contador) +
                            palabra_codificada[pos + contador:])
        contador += 1
    
    palabra_codificada += 'ay'
   
    return palabra_codificada

def main():
    entrada = input()
    palabra_codificada = codificar_palabra(entrada)
    print(palabra_codificada)

main()
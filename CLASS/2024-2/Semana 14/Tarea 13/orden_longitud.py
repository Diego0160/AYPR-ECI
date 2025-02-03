"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Orden por longitud
===========================================
Fecha: 19 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def ordenar(text):
    """ Ordena las palabras de un texto por longitud.
    (str) -> str """
    words = text.split()
    words.sort(key=len)
    return ' '.join(words)

def main():
    entrada = input()
    Texto_ordenado = ordenar(entrada)
    print(Texto_ordenado)

main()
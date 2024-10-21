"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Invertir
=========================================
Fecha: 10 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def invertir(elements):
    """Invierte los elementos de una lista
       n > 0
       (list) -> list"""
    cantidad = len(elements)
    for i in range(cantidad // 2):
        elements[i], elements[cantidad - i - 1] = elements[cantidad - i - 1], elements[i]
    return elements

def main():
    entrada = input()
    elements = entrada.split(',')
    invertir(elements)
    ai = invertir(elements)
    print(','.join(ai))

main()
"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Librería editor_texto
=========================================
Fecha: 17 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
l_max = 72

def alinear_izquierda(texto):
    """ Alinea un texto a la izquierda dentro de un ancho máximo.
    Si el texto es más largo que el ancho máximo, se divide en líneas.
    (str) -> str
    """
    if len(texto) <= l_max:
        return texto.ljust(l_max)
    else:
        return texto[:l_max].ljust(l_max) + '\n' + alinear_izquierda(texto[l_max:])

def alinear_derecha(texto):
    """ Alinea un texto a la derecha dentro de un ancho máximo.
    Si el texto es más largo que el ancho máximo, se divide en líneas.
    (str) -> str
    """
    if len(texto) <= l_max:
        return texto.rjust(l_max)
    else:
        return texto[:l_max].rjust(l_max) + '\n' + alinear_derecha(texto[l_max:])

def centrar_texto(texto):
    """ Centra un texto dentro de un ancho máximo.
    Si el texto es más largo que el ancho máximo, se divide en líneas.
    (str) -> str
    """
    if len(texto) <= l_max:
        return texto.center(l_max)
    else:
        return texto[:l_max].center(l_max) + '\n' + centrar_texto(texto[l_max:])

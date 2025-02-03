"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Repeticiones
=========================================
Fecha: 23 de Septiembre de 2024
=========================================
"""
def saludo_recurrente(cont):
    """ Imprime un saludo varias veces usando recurrencia
    (int) -> None
    """
    print("Hola", cont)
    if cont == 5:
        print("Fin")
    else:
        cont += 1
        saludo_recurrente(cont)

def saludo_repetitivo(cont = 1):
    """ Imprime un saludo de manera repetida usando iteracion
    (int) -> None
    """
    while cont <= 5:
        print("Hola", cont)
        cont += 1
    #end_while
    print("Fin")
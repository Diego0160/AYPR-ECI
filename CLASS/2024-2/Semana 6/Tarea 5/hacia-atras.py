"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Hacia Atrás
=========================================
Fecha: 17 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def hacia_atras(n):
    """ Genera una cadena que muestra el número n repetido n veces, seguido de un asterisco y la secuencia hacia atrás hasta 1.
    (int) -> str
    """
    if n == 1:
        return "1"
    else:
        return str(n) * n + '*' + hacia_atras(n - 1)

def main():
    numero = int(input("Ingrese un número entero positivo: "))
    
    if numero <= 0:
        print("Debe ingresar un número entero positivo.")
    else:
        print(hacia_atras(numero))

main()


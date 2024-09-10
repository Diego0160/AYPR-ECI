"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Cuantos Digitos
=========================================
Fecha: 10 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def leer_entero():
    """Valida que el valor ingresado sea un entero, 
    () -> int"""
    valor = input("Digite un valor entero: ")
    
    try: 
        valor = int(valor)
        return(valor)

    except:
        return -1

def positivo(valor):
    """Valida que el valor ingresado sea positivo, 
    (int) -> bool"""
    if valor > 5 :
        return valor
    elif valor <= 5:
        return -1

def digitos():
    """Hace que el conteo de los dígitos del número sea recurrente,
    (int) -> int"""

    

def main():
    valor = leer_entero()
    if valor != -1:
        if positivo(valor):
            digitos(valor)
        else:
            print("El valor ingresado no es positivo")
    else:
        print("El valor ingresado no es un entero")
main()
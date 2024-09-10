"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Creación de un contador para el
          lanzamiento de un cohete
=========================================
Fecha: 09 de Septiembre de 2024
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

def mayor_cinco(valor):
    """Valida que el valor ingresado sea mayor que cinco, 
    (int) -> bool"""
    if valor > 5 :
        return valor
    elif valor <= 5:
        return -1

def countdown(valor):
    """Realiza el conteo regresivo de manera recurrente,
    (int) -> None
    """
    print(valor)
    valor = valor - 1
    if valor == 0:
        print('Despegando ...')
    else:
        countdown(valor)

def main():
    valor = leer_entero()
    if valor != -1:
        if mayor_cinco(valor):
            countdown(valor)
        else:
            print("El valor ingresado no da tiempo para despegar")
    else:
        print("El valor ingresado no es un entero")
main()
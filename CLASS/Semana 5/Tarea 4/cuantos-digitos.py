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
        return valor
    except:
        return -1

def positivo(valor):
    """Valida que el valor ingresado sea positivo, 
    (int) -> bool"""
    return valor > 0

def digitos(valor):
    """Hace que el conteo de los dígitos del número sea recurrente,
    (int) -> int"""
    if valor < 10:
        return 1
    else:
        return 1 + digitos(valor // 10)

def main():
    valor = leer_entero()
    if valor != -1:
        if positivo(valor):
            cantidad_d = digitos(valor)
            print(cantidad_d)
        else:
            print("El valor ingresado no es positivo")
    else:
        print("El valor ingresado no es un entero")

main()
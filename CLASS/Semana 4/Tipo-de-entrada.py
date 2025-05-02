"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Determinar el tipo de valor de 
          entrada.
=========================================
Fecha: 5 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def main():
    valor = input("Digite un valor entero: ")
    
    try: 
        valor = int(valor)
        print('Es un valor entero')
    except:
        print('No es un valor entero')

main()

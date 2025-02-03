"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Previa: Producto
Tematica: Algorítmos con condicionales 
          repetitivos
=========================================
Fecha: 3 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def main():
    # Creamos una lista vacía para almacenar los números ingresados
    numeros = []

    while True:
        # Solicitamos al usuario que ingrese un número
        num = int(input("Ingrese un número: "))
        
        # Si el usuario ingresa 0 y la lista de números está vacía
        if num == 0:
            if not numeros:
                # Imprimimos "Nada" y salimos de la función
                print("Nada")
                return
            else:
                # Si hay números en la lista, multiplicamos cada número por los demás
                producto = 1
                for x in numeros:
                    producto = producto * x
                # Imprimimos el resultado de la multiplicación
                print("Resultado:", producto)
                return
        else:
            # Si el número ingresado no es 0, lo agregamos a la lista
            numeros.append(num)
main()
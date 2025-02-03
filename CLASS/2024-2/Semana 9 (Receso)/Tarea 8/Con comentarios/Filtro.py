"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Filtro
=========================================
Fecha: 10 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def filtro_numeros_mayores(secuencia, numero):
    """Filtra los números de la secuencia que son mayores que el número dado.
       (list, int) -> list"""
    # Convertimos la secuencia de números a una lista de flotantes
    numeros = list(map(float, secuencia.split()))
    # Filtramos los números que son mayores que el número dado
    resultado = [num for num in numeros if num > numero]
    return resultado

def main():
    # Pedimos al usuario que ingrese la secuencia de números reales en la primera línea
    secuencia = input("Ingresa la secuencia de números reales: ")
    # Pedimos al usuario que ingrese el número entero en la segunda línea
    numero = int(input("Ingresa el número entero: "))
    # Llamamos a la función filtro_numeros_mayores
    filtro_numeros_mayores(secuencia, numero)
    # Llamamos a la función filtrar_numeros_mayores para obtener la lista filtrada
    resultado = filtro_numeros_mayores(secuencia, numero)
    # Imprimimos la lista filtrada
    print(resultado)

# Llamamos a la función principal para ejecutar el programa
main()

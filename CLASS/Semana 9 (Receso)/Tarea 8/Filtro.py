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
    numeros = list(map(float, secuencia.split()))
    resultado = [num for num in numeros if num > numero]
    return resultado

def main():
    secuencia = input("Ingresa la secuencia de números reales: ")
    numero = int(input("Ingresa el número entero: "))
    filtro_numeros_mayores(secuencia, numero)
    resultado = filtro_numeros_mayores(secuencia, numero)
    print(resultado)

main()
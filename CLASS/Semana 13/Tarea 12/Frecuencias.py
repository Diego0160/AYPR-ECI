"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Frecuencias
===========================================
Fecha: 12 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def obtener_numeros_unicos(lista):
    """ Obtiene una lista ordenada de números sin repetir 
    (list) -> list """
    unicos = []
    for num in lista:
        if num not in unicos:
            unicos.append(num)
    return sorted(unicos)

def contar_frecuencias(lista, numero):
    """ Cuenta cuántas veces aparece un número en la lista 
    (list, int) -> int """
    contador = 0
    for num in lista:
        if num == numero:
            contador += 1
    return contador

def main():
    ns = input()
    numeros = [int(x) for x in ns.split()]
    
    numeros_unicos = obtener_numeros_unicos(numeros)
    
    for num in numeros_unicos:
        frecuencia = contar_frecuencias(numeros, num)
        print(f"{num}: {frecuencia}")

main()
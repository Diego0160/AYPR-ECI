"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Conjetura de Goldbach
===========================================
Fecha: 12 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def es_primo(numero):
    """ Verifica si un número es primo 
    (int) -> bool """
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_suma_primos(numero):
    """ Encuentra dos números primos que sumen el número dado 
    (int) -> tuple """
    for i in range(2, numero):
        if es_primo(i) and es_primo(numero - i):
            return (i, numero - i)
    return None

def main():
    numero = int(input())
    
    if numero <= 2 or numero % 2 != 0:
        print("El número debe ser par y mayor que 2")
        return
    
    primos = encontrar_suma_primos(numero)
    if primos is not None:
        print(f"{primos[0]} + {primos[1]}")
    else:
        print("No se encontraron dos números primos que sumen el número dado.")

main()
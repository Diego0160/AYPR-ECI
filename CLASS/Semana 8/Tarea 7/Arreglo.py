"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Crear Arreglo
=========================================
Fecha: 1 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def crear_arreglo(cantidad):
    elementos = []
    for i in range(cantidad):
        elemento = input()
        elementos.append(elemento)
    return elementos

def main():
    cantidad = int(input())
    arreglo = crear_arreglo(cantidad)
    print(arreglo)

main()
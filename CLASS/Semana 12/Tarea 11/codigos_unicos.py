"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Códigos únicos
===========================================
Fecha: 5 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""

def calcular_suma(paquete, destinatario):
    """ Calcula la suma de dos numeros enteros
    (int, int) -> int """
    return paquete + destinatario

def generar_codigo_unico(paquete, destinatario):
    """ Genera el codigo unico a partir de la suma y los numeros dados anteriormente
    (int, int) -> str """
    suma = calcular_suma(paquete, destinatario)
    codigo_unico = str(suma) + str(paquete) + str(destinatario)
    return codigo_unico

def main():
    paquete = int(input())
    destinatario = int(input())
    codigo = generar_codigo_unico(paquete, destinatario)
    print(codigo)

main()

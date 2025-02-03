"""
from sys import stdin, stdout, stderr
# leer una linea hasta un salto de linea
dato = stdin.readline()
"""

# Programa uso entrada y salida estandar
import sys

def main():
    dato = input("Hola digite algo")
    sys.stdout.write("Salida usando write() " + dato)
    dato = sys.stdin.readline()
    print("Salida usando print()", dato)
    print("Longitud del valor de dato", len(dato))
    # entrada usando input()
    dato = input("Hola digite algo")
    print("Longitud del valor de dato", len(dato))
main()


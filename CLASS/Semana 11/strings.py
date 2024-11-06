"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Strings
Objetivo: 1. Identificar y hacer operaciones 
          con datos tipo string.
          2. Conocer funciones y métodos de 
          la clase string.
          3. Seguir practicando la escritura 
          y usos de subprogramas con uso de 
          parámetros y retornos.
===========================================
Fecha: 31 de Octubre de 2024
Autor: Diego Prado Pardo
===========================================
"""

import random
import string

def contar_letras(nombre):
    """Cuenta la cantidad de letras en el nombre.
    (str) -> int"""
    return sum(1 for char in nombre if char.isalpha())

def contar_vocales(nombre):
    """Cuenta la cantidad de vocales en el nombre.
    (str) -> int"""
    vocales = 'aeiouAEIOU'
    return sum(1 for char in nombre if char in vocales)

def contar_vocal_especifica(nombre, vocal):
    """Cuenta cuántas veces aparece una vocal dada.
    (str, str) -> int"""
    return nombre.lower().count(vocal.lower())

def convertir_mayusculas(nombre):
    """Convierte todo el nombre a mayúsculas.
    (str) -> str"""
    return nombre.upper()

def convertir_minusculas(nombre):
    """Convierte todo el nombre a minúsculas.
    (str) -> str"""
    return nombre.lower()

def separar_nombres_apellidos(nombre):
    """Separa cada nombre y apellido en una lista.
    (str) -> list"""
    return nombre.split()

def capitalizar_primera_letra(nombre):
    """Convierte solo la primera letra de cada nombre en mayúscula.
    (str) -> str"""
    return nombre.title()

def contar_cadenas(nombre):
    """Cuenta cuántas cadenas componen el nombre.
    (str) -> int"""
    return len(separar_nombres_apellidos(nombre))

def posiciones_letra(nombre, letra):
    """Encuentra las posiciones de una letra dada en el nombre.
    (str, str) -> list"""
    return [i for i, char in enumerate(nombre) if char.lower() == letra.lower()]

def diminutivo(nombre):
    """Construye dos opciones de diminutivo para el primer nombre.
    (str) -> tuple"""
    primer_nombre = nombre.split()[0]
    diminutivo1 = primer_nombre + 'ito'
    diminutivo2 = primer_nombre[:len(primer_nombre) - 1] + 'sito'
    return diminutivo1, diminutivo2

def letra_menor_valor(nombre):
    """Encuentra la letra con el menor valor ASCII en el nombre.
    (str) -> str"""
    letras = [char for char in nombre if char.isalpha()]
    return min(letras) if letras else None

def letra_mayor_valor(nombre):
    """Encuentra la letra con el mayor valor ASCII en el nombre.
    (str) -> str"""
    letras = [char for char in nombre if char.isalpha()]
    return max(letras) if letras else None

def crear_direccion_email(nombre, dominio):
    """Crea una dirección de correo electrónico.
    (str, str) -> str"""
    nombres = nombre.split()
    email = '.'.join(n.lower() for n in nombres) + '@' + dominio
    return email

def generar_contraseña(nombre):
    """Genera una contraseña válida según los requisitos del taller.
    (str) -> str"""
    while True:
        longitud = random.randint(8, 12)
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        
        if (any(c.isupper() for c in contraseña) and
            any(c.islower() for c in contraseña) and
            any(c.isdigit() for c in contraseña) and
            any(c in "!@#$%^&*" for c in contraseña) and
            all(contraseña[i:i+3].lower() not in nombre.lower() for i in range(len(contraseña) - 2))):
            return contraseña

def main():
    nombre = input("Ingrese su nombre completo: ")
    print("\nDigite el número que desea ejecutar:")
    print("1: Contar la cantidad de letras en el nombre")
    print("2: Contar la cantidad de vocales en el nombre")
    print("3: Contar cuántas veces aparece una vocal dada")
    print("4: Convertir todo el nombre a mayúsculas")
    print("5: Convertir todo el nombre a minúsculas")
    print("6: Separar cada nombre y apellido en una lista")
    print("7: Capitalizar solo la primera letra de cada nombre")
    print("8: Contar cuántas cadenas componen el nombre")
    print("9: Encontrar las posiciones de una letra dada")
    print("10: Generar dos diminutivos para el primer nombre")
    print("11: Explicar qué es la tabla ASCII")
    print("12: Encontrar la letra con el menor valor ASCII en el nombre")
    print("13: Encontrar la letra con el mayor valor ASCII en el nombre")
    print("14: Explicar los comandos chr() y ord()")
    print("15: Crear una dirección de correo electrónico")
    print("16: Generar una contraseña válida")
    print("0: Salir del programa") #Opcional, es para darle mas detalles al código
    
    while True:        
        opcion = int(input("\nIngrese una opción: "))
        
        if opcion == 0:
            print("Saliendo del programa...")
            break
        elif opcion == 1:
            print("Cantidad de letras:", contar_letras(nombre))
        elif opcion == 2:
            print("Cantidad de vocales:", contar_vocales(nombre))
        elif opcion == 3:
            vocal = input("Ingrese una vocal para contar sus apariciones: ")
            print(f"Cantidad de veces que aparece la vocal '{vocal}':", contar_vocal_especifica(nombre, vocal))
        elif opcion == 4:
            print("Nombre en mayúsculas:", convertir_mayusculas(nombre))
        elif opcion == 5:
            print("Nombre en minúsculas:", convertir_minusculas(nombre))
        elif opcion == 6:
            print("Lista de nombres y apellidos:", separar_nombres_apellidos(nombre))
        elif opcion == 7:
            print("Nombre con primeras letras en mayúsculas:", capitalizar_primera_letra(nombre))
        elif opcion == 8:
            print("Cantidad de cadenas en el nombre:", contar_cadenas(nombre))
        elif opcion == 9:
            letra = input("Ingrese una letra para encontrar sus posiciones: ")
            print(f"Posiciones de la letra '{letra}':", posiciones_letra(nombre, letra))
        elif opcion == 10:
            diminutivo1, diminutivo2 = diminutivo(nombre)
            print("Diminutivo 1:", diminutivo1)
            print("Diminutivo 2:", diminutivo2)
        elif opcion == 11:
            print("ASCII: Es un sistema de codificación de caracteres en el que cada símbolo está representado por un número.")
        elif opcion == 12:
            print("Letra con el menor valor:", letra_menor_valor(nombre))
        elif opcion == 13:
            print("Letra con el mayor valor:", letra_mayor_valor(nombre))
        elif opcion == 14:
            print("chr(): Convierte un código ASCII en su correspondiente carácter.")
            print("ord(): Convierte un carácter en su correspondiente código ASCII.")
        elif opcion == 15:
            dominio = input("Ingrese el dominio de correo electrónico: ")
            print("Dirección de correo electrónico:", crear_direccion_email(nombre, dominio))
        elif opcion == 16:
            print("Contraseña generada:", generar_contraseña(nombre))
        else:
            print("Opción no válida. Por favor seleccione un número entre 0 y 16.")

main()
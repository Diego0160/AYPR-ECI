"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Editor
=========================================
Fecha: 17 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
import libreria_editor_texto as let

l_max = 50

def main():
    mensaje = input(f"Ingrese el mensaje (máximo {l_max} caracteres): ")
    
    if len(mensaje) > l_max:
        print(f"El mensaje no puede ser mayor a {l_max} caracteres.")
        return
    
    opcion = input("Ingrese la alineación (izquierda, derecha, centrado): ").lower()
    
    if opcion == "izquierda" or opcion == "i":
        print(let.alinear_izquierda(mensaje))
    elif opcion == "derecha" or opcion == "d":
        print(let.alinear_derecha(mensaje))
    elif opcion == "centrado" or opcion == "c":
        print(let.centrar_texto(mensaje))
    else:
        print("Opción inválida. Por favor, elija entre 'izquierda', 'derecha' o 'centrado'.")

main()

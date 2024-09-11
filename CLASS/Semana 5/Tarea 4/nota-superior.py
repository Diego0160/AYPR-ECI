"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Nota Superior
=========================================
Fecha: 10 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
# Extra: Se importa random para el uso de una funcion que obtenga una frase cada vez que se solicite
import random

def mensaje_motivador():
    """Devuelve un mensaje motivador aleatorio
    () -> str"""
    mensajes = [
        "¡Sigue así, vas por buen camino!",
        "¡No te rindas, el esfuerzo trae recompensas!",
        "¡Con un poco más de esfuerzo lo lograrás!",
        "¡No te preocupes, puedes mejorar la próxima vez!",
        "¡Tú puedes, sigue intentándolo!"
    ]
    return random.choice(mensajes)

def promedio(nota1, nota2, nota3):
    """Calcula el promedio de tres valores,
    (float, float, float) -> float"""
    return (nota1 + nota2 + nota3) / 3

def main():

    notas = input("Ingrese tres notas separadas por espacio: ")
    nota1, nota2, nota3 = map(float, notas.split())
    nota_promedio = promedio(nota1, nota2, nota3)
    
    if nota_promedio >= 4.5:
        print("¡Felicidades! Obtuvo una nota superior.")
    elif nota1 >= 4.5 or nota2 >= 4.5 or nota3 >= 4.5:
        print(mensaje_motivador())
    else:
        print()

main()
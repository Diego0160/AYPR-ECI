"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Trio o escalera
=========================================
Fecha de inicio: 3 de Octubre de 2024
Fecha de fin: 10 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""
import random

def repartir_cartas():
    """Reparte 4 cartas aleatorias con valores del 1 al 9"""
    return [random.randint(1, 9) for _ in range(4)]

def ordenar_cartas(cartas):
    """Ordena las cartas usando el algoritmo de burbuja (bubble sort)"""
    n = len(cartas)
    for i in range(n):
        for j in range(0, n-i-1):
            if cartas[j] > cartas[j+1]:
                cartas[j], cartas[j+1] = cartas[j+1], cartas[j]

def es_trio(cartas):
    """Verifica si hay tres cartas del mismo valor"""
    return cartas[0] == cartas[1] == cartas[2] or cartas[1] == cartas[2] == cartas[3]

def es_escalera(cartas):
    """Verifica si las cartas forman una escalera"""
    return cartas[1] == cartas[0] + 1 and cartas[2] == cartas[1] + 1 and cartas[3] == cartas[2] + 1

def cambiar_carta(cartas):
    """Permite al jugador cambiar una carta"""
    print("Tus cartas actuales son:", cartas)
    carta_a_cambiar = int(input("¿Qué carta deseas cambiar? (1-4) o ingresa 0 para no cambiar: "))
    
    if 1 <= carta_a_cambiar <= 4:
        nueva_carta = random.randint(1, 9)
        print(f"Carta {carta_a_cambiar} cambiada. Nueva carta: {nueva_carta}")
        cartas[carta_a_cambiar - 1] = nueva_carta
        ordenar_cartas(cartas)
    else:
        print("No se ha cambiado ninguna carta.")
    
    print("Tus cartas ahora son:", cartas)

def main():
    print("¡Bienvenido al juego de Trío o Escalera!")
    
    while True:
        cartas = repartir_cartas()
        print("\nSe reparten las cartas...")
        ordenar_cartas(cartas)
        print("Tus cartas ordenadas son:", cartas)
        
        if es_trio(cartas):
            print("¡Felicidades, tienes un trío! Has ganado.")
        elif es_escalera(cartas):
            print("¡Felicidades, tienes una escalera! Has ganado.")
        else:
            print("No tienes ni trío ni escalera.")
            respuesta = input("¿Quieres cambiar una carta? (s/n): ").lower()
            if respuesta == 's':
                cambiar_carta(cartas)
                if es_trio(cartas):
                    print("¡Felicidades, tienes un trío! Has ganado.")
                elif es_escalera(cartas):
                    print("¡Felicidades, tienes una escalera! Has ganado.")
                else:
                    print("No lograste formar ni trío ni escalera. ¡Has perdido!")
            else:
                print("No lograste formar ni trío ni escalera. ¡Has perdido!")
        
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar.")
            break

main()
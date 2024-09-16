"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Carrera de observación
=========================================
Fecha: 12 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
from random import randint
from time import sleep

estacion6_alcanzada = False

def punto_partida(pts, mensaje=None):
    """Función que retorna un número aleatorio entre 1 y 20 y opcionalmente muestra un mensaje.
    (int, str) -> int"""
    if mensaje:
        print(mensaje)
    return randint(1, 20)

def num_primo(n, divisor=None):
    """Función que verifica si un número es primo.
    (int, int) -> bool"""
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return num_primo(n, divisor - 1)

def mensaje1(origen):
    """Función que muestra un mensaje para regresar a la estación indicada y simula la acción de continuar.
    (int) -> None"""
    print()
    ini = input(f'Presione el acelerador para regresar a la estación {origen} ...')
    print()
    print(f'Regresando a la estación {origen}')
    sleep(1)
    print(f'Saliendo de la estación {origen}')
    sleep(1)
    print()
    ini = input(f'Presione el acelerador para continuar ...')
    sleep(1.5)

def estacion_comidas(pts, origen):
    """Función donde se ganan 100 puntos si se regresa a la estación correcta.
    (int, int) -> int"""
    print()
    sleep(0.5)
    print('Ingresando a la estación comidas ...')
    sleep(1)
    print("Bienvenido, llegaste a comidas, buen apetito")
    pts = pts + 100
    sleep(1)
    try:
        regreso = int(input("Diga el número de la estación a la que regresa: "))
    except:
        print("Entrada inválida, pierdes 20 puntos.")
        mensaje1(origen)
        return pts - 20
    
    if regreso == origen:
        resultado = pts 
    else:
        print("Penalización, la estación dada no coincide con el origen.")
        resultado = pts - randint(1, 20)

    mensaje1(origen)

    return resultado

def estacion_desinfle(pts, origen):
    """Función donde se pierden puntos si no se regresa a la estación correcta.
    (int, int) -> int"""
    print()
    sleep(0.5)
    print('Ingresando a la estación desinfle ...')
    sleep(1)
    print("Lo sentimos, llegó a desinfle.")
    pts -= 30
    try:
        regreso = int(input("Diga número de la estación a la que regresa: "))
    except:
        print("Entrada inválida, pierdes 10 puntos adicionales.")
        mensaje1(origen)
        return pts - 10
    
    if regreso == origen:
        print("Regreso correcto.")
    else:
        print("Penalización, la estación dada no coincide con el origen.")
        pts = pts - randint(1, 20)

        return 
    
    mensaje1(origen)

    return pts

def estacion1(pts):
    """Función donde se pide un número impar. Si es correcto, suma puntos.
    (int) -> int"""
    print()
    print('Bienvenido a la Estación 1')
    sleep(0.5)
    try:
        num = int(input('Digite un número impar: '))
        if num % 2 != 0:
            print("Correcto, ganas 5 puntos.")
            return estacion_comidas(pts + 5, 1)
        else:
            print("Incorrecto, pierdes 3 puntos.")
            return pts - 3
    except:
        print("Entrada inválida. Inténtalo de nuevo.")
        return estacion1(pts)

def estacion2(pts):
    """Función donde se pide un número múltiplo de 6 y 8. Si es correcto, suma puntos.
    (int) -> int"""
    print()
    print('Bienvenido a la Estación 2')
    sleep(0.5)
    try:
        num = int(input('Digite un número que sea múltiplo de 6 y de 8: '))
        if num % 6 == 0 and num % 8 == 0:
            print("Correcto, ganas 10 puntos.")
            return pts + 10
        else:
            print("Incorrecto, no ganas puntos.")
            return pts
    except:
        print("Entrada inválida. Inténtalo de nuevo.")
        return estacion2(pts)

def estacion3(pts):
    """Función donde se pide una palabra de cuatro letras que contenga dos 'a'.
    (int) -> int"""
    print()
    print('Bienvenido a la Estación 3')
    sleep(0.5)
    word = input('Digite una palabra de cuatro letras que contenga dos vocales "a": ').lower()
    
    if len(word) == 4 and word.count('a') == 2:
        print("Correcto, ganas 6 puntos.")
        return estacion_comidas(pts + 6, 3)
    else:
        print("Incorrecto, pierdes 8 puntos.")
        return estacion_desinfle(pts - 8, 3)

def estacion4(pts):
    """Función donde se piden tres números primos que sumen 63.
    (int) -> int"""
    global estacion6_alcanzada
    print()
    print('Bienvenido a la Estación 4')
    sleep(0.5)
    try:
        num1 = int(input('Digite el primer número primo: '))
        num2 = int(input('Digite el segundo número primo: '))
        num3 = int(input('Digite el tercer número primo: '))

        if num1 + num2 + num3 == 63 and num_primo(num1) and num_primo(num2) and num_primo(num3):
            print("Correcto, ganas 25 puntos.")
            estacion6_alcanzada = True
            return estacion6(pts + 25)
        else:
            print("Incorrecto, pierdes 2 puntos.")
            return pts - 2
    except:
        print("Entrada inválida. Inténtalo de nuevo.")
        return estacion4(pts)

def estacion5(pts):
    """Función donde se piden dos números cuya suma sea 13 y su producto sea 42.
    (int) -> int"""
    global estacion6_alcanzada
    if estacion6_alcanzada:
        return pts
    
    print()
    print('Bienvenido a la Estación 5')
    sleep(0.5)
    try:
        num1 = int(input('Digite el primer número: '))
        num2 = int(input('Digite el segundo número: '))
        
        if num1 + num2 == 13 and num1 * num2 == 42:
            print("Correcto, ganas 5 puntos.")
            return pts + 5
        else:
            print("Incorrecto, pierdes 1 punto.")
            return pts - 1
    except:
        print("Entrada inválida. Inténtalo de nuevo.")
        return estacion5(pts)

def estacion6(pts):
    """Función donde se pide una palabra de cinco letras que termine en 'al'.
    (int) -> int"""
    global estacion6_alcanzada
    print()
    print('Bienvenido a la Estación 6')
    sleep(0.5)
    palabra = input('Digite una palabra de cinco letras que termine en "al": ').lower()
    
    if len(palabra) == 5 and palabra.endswith("al"):
        print("Correcto, ganas 5 puntos.")
        estacion6_alcanzada = True
        return pts + 5
    else:
        print("Incorrecto, pierdes 2 puntos.")
        return pts - 2

def main():
    pts = punto_partida(0)
    print("Bienvenidos a la carrera de observación usando funciones y parámetros.")
    ini = input("Presione Enter para iniciar ...")
    print("Inicias con " + str(pts) + " puntos")
    
    pts = estacion1(pts)
    pts = estacion2(pts)
    pts = estacion3(pts)
    pts = estacion4(pts)

    print("\nRegresando al punto de partida")
    if pts > 130:
        pts = punto_partida(pts, "¡Felicidades! Ganas un viaje a la luna con todos los gastos pagados.")
    elif pts > 50:
        pts = punto_partida(pts, "¡Felicidades! Ganas un viaje al polo sur una semana con los pingüinos.")
    else:
        pts = punto_partida(pts, "¡Felicidades! Ganas una cena en la nave interestelar con crucero por la galaxia (sin desembarcos).")
    
    print("\nFin de la carrera")

main()



def estacion_comidas(pts, origen):
    """Función donde se ganan 100 puntos si se regresa a la estación correcta.
    (int, int) -> int"""
    print()
    sleep(0.5)
    print('Ingresando a la estación comidas ...')
    sleep(1)
    print("Bienvenido, llegaste a comidas, buen apetito")
    pts = pts + 100
    sleep(1)
    try:
        regreso = int(input("Diga el número de la estación a la que regresa: "))
    except:
        print("Entrada inválida, pierdes 20 puntos.")
        pts -= 20
        mensaje1(origen)
        return pts
    
    if regreso == origen:
        print("Regreso correcto.")
    else:
        print("Penalización, la estación dada no coincide con el origen.")
        pts = pts - randint(1, 20)

    mensaje1(origen)  # Siempre regresar a la estación original
    return pts

def estacion_desinfle(pts, origen):
    """Función donde se pierden puntos si no se regresa a la estación correcta.
    (int, int) -> int"""
    print()
    sleep(0.5)
    print('Ingresando a la estación desinfle ...')
    sleep(1)
    print("Lo sentimos, llegó a desinfle.")
    pts -= 30
    try:
        regreso = int(input("Diga número de la estación a la que regresa: "))
    except:
        print("Entrada inválida, pierdes 10 puntos adicionales.")
        pts -= 10
        mensaje1(origen)
        return pts
    
    if regreso == origen:
        print("Regreso correcto.")
    else:
        print("Penalización, la estación dada no coincide con el origen.")
        pts = pts - randint(1, 20)

    mensaje1(origen)  # Siempre regresar a la estación original
    return pts

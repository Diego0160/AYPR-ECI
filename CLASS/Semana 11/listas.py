"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: Listas
Objetivo: Conocer, estudiar y comprender 
          conceptos básicos de los arreglos 
          y su implementación como listas 
          y cómo usarlos.
===========================================
Fecha: 31 de Octubre de 2024
Autor: Diego Prado Pardo
===========================================
"""

def secuencia_valores(v):
    """ Imprime los valores de la lista en una sola línea, separados por espacios.
    (list) -> None """
    print(" ".join(map(str, v)))

def linea(lista):
    """ Imprime cada valor de la lista en una línea separada.
    (list) -> None """
    for v in lista:
        print(v)

def cantidad_elementos(lista):
    """ Devuelve la cantidad de elementos en la lista.
    (list) -> int """
    return len(lista)

def cantidad_pares(lista):
    """ Devuelve la cantidad de elementos pares en la lista.
    (list) -> int """
    return sum(1 for v in lista if v % 2 == 0)

def mitad_hasta_final(lista):
    """ Imprime los elementos desde la mitad de la lista hasta el final.
    (list) -> None """
    for i in range(len(lista) // 2, len(lista)):
        print(lista[i])

def imprimir_pares(lista):
    """ Imprime los elementos en posiciones pares de la lista.
    (list) -> None """
    for i in range(0, len(lista), 2):
        print(lista[i])

def separar_listas(lista):
    """ Separa la lista en dos mitades.
    (list) -> tuple """
    mitad = len(lista) // 2
    primera_mitad = lista[:mitad]
    segunda_mitad = lista[mitad:]
    return primera_mitad, segunda_mitad

def concatenar_listas(lista1, lista2):
    """ Concatena dos listas en el orden de lista2 + lista1.
    (list, list) -> list """
    return lista2 + lista1

def menor_valor(lista):
    """ Devuelve el menor valor en la lista.
    (list) -> int """
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor

def mayor_valor(lista):
    """ Devuelve el mayor valor en la lista.
    (list) -> int """
    mayor = lista[0]
    for valor in lista:
        if valor > mayor:
            mayor = valor
    return mayor

def buscar_valor(lista, valor):
    """ Busca un valor en la lista y devuelve su índice, o -1 si no está presente.
    (list, int) -> int """
    for i, v in enumerate(lista):
        if v == valor:
            return i
    return -1

def posicion_valor(lista, valor):
    """ Devuelve la posición de un valor dado en la lista.
    (list, int) -> int """
    return buscar_valor(lista, valor)

def modificar_segundo(lista, nuevo_valor):
    """ Modifica el segundo elemento de la lista.
    (list, int) -> list """
    lista[1] = nuevo_valor
    return lista

def eliminar_ultimo(lista):
    """ Elimina el último elemento de la lista.
    (list) -> list """
    return lista[:-1]

def eliminar_valor(lista, valor):
    """ Elimina la primera aparición de un valor dado de la lista.
    (list, int) -> list """
    lista_copia = lista[:]
    lista_copia.remove(valor)
    return lista_copia

def insertar_posicion(lista, valor, posicion):
    """ Inserta un valor en una posición específica de la lista.
    (list, int, int) -> list """
    lista_copia = lista[:]
    lista_copia.insert(posicion, valor)
    return lista_copia

def insertar_primero(lista, valor):
    """ Inserta un valor en la primera posición de la lista.
    (list, int) -> list """
    return [valor] + lista

def agregar_elemento(lista, valor):
    """ Agrega un valor al final de la lista.
    (list, int) -> list """
    lista_copia = lista[:]
    lista_copia.append(valor)
    return lista_copia

def imprimir_lista(lista):
    """ Imprime la lista con corchetes y comas.
    (list) -> None """
    print(lista)

def imprimir_inversa(lista):
    """ Imprime la lista en orden inverso sin modificarla.
    (list) -> None """
    print(lista[::-1])

def invertir_lista(lista):
    """ Invierte los elementos de la lista y la imprime junto con la original.
    (list) -> list """
    lista_inversa = lista[::-1]
    print("Original:", lista)
    print("Inversa:", lista_inversa)
    return lista_inversa

def suma_valores(lista):
    """ Calcula la suma de los valores en la lista.
    (list) -> int """
    total = 0
    for valor in lista:
        total += valor
    return total

def ordenar_lista(lista):
    """ Ordena la lista e imprime los elementos separados por guiones.
    (list) -> list """
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    print("-".join(map(str, lista)))
    return lista

def duplicar_lista(lista):
    """ Duplica los valores de la lista e imprime la original y la copia.
    (list) -> list """
    lista_copia = [x * 2 for x in lista]
    print("Original:", lista)
    print("Copia:", lista_copia)
    return lista_copia

def obtener_porcion(lista, a, b):
    """ Devuelve una porción de la lista entre las posiciones a y b (inclusive).
    (list, int, int) -> list """
    return lista[a:b+1]

def main():
    valores = input("Ingrese una lista de valores separados por comas:\n")
    lista = list(map(int, valores.split(",")))
    print(lista)
    print("\nDigite el número que desea ejecutar:\n2: Imprimir valores en una sola línea separados por espacios\n3: Imprimir valores en líneas separadas\n4: Contar la cantidad de elementos en la lista\n5: Contar la cantidad de valores pares en la lista\n6: Imprimir elementos desde la mitad hasta el final\n7: Imprimir elementos en posiciones pares\n8: Separar la lista en dos mitades\n9: Concatenar las dos mitades (segunda mitad primero)\n10: Obtener el menor valor en la lista\n11: Obtener el mayor valor en la lista\n12: Buscar un valor y devolver su posición\n13: Obtener la posición de un valor específico\n14: Modificar el segundo elemento de la lista\n15: Eliminar el último elemento de la lista\n16: Eliminar una aparición de un valor dado\n17: Insertar un valor en una posición específica\n18: Insertar un valor en la primera posición\n19: Agregar un valor al final de la lista\n20: Imprimir la lista completa (con corchetes y comas)\n21: Imprimir la lista en orden inverso (sin modificarla)\n22: Invertir la lista y mostrar la original junto a la invertida\n23: Calcular la suma de los valores en la lista\n24: Ordenar los elementos y mostrarlos con guiones\n25: Hacer una copia de la lista y duplicar sus valores\n26: Obtener una porción de la lista entre dos posiciones\n0: Salir del programa")
    
    while True:
        print("\nDigite el número que desea ejecutar:")
        opcion = int(input())
        
        if opcion == 0: #Opcional, es para darle mas detalles al código
            print("Saliendo del programa...")
            break
        elif opcion == 2:
            secuencia_valores(lista)
        elif opcion == 3:
            linea(lista)
        elif opcion == 4:
            print("Cantidad de elementos:", cantidad_elementos(lista))
        elif opcion == 5:
            print("Cantidad de elementos pares:", cantidad_pares(lista))
        elif opcion == 6:
            mitad_hasta_final(lista)
        elif opcion == 7:
            imprimir_pares(lista)
        elif opcion == 8:
            primera_mitad, segunda_mitad = separar_listas(lista)
            print("Primera mitad:", primera_mitad)
            print("Segunda mitad:", segunda_mitad)
        elif opcion == 9:
            primera_mitad, segunda_mitad = separar_listas(lista)
            print("Concatenación de listas:", concatenar_listas(primera_mitad, segunda_mitad))
        elif opcion == 10:
            print("Menor valor:", menor_valor(lista))
        elif opcion == 11:
            print("Mayor valor:", mayor_valor(lista))
        elif opcion == 12:
            valor_a_buscar = int(input("Ingrese el valor a buscar en la lista: "))
            print("Posición del valor:", posicion_valor(lista, valor_a_buscar))
        elif opcion == 13:
            valor_a_buscar = int(input("Ingrese el valor a buscar en la lista: "))
            print("Posición del valor:", posicion_valor(lista, valor_a_buscar))
        elif opcion == 14:
            nuevo_valor = int(input("Ingrese el nuevo valor para el segundo elemento: "))
            print("Lista modificada:", modificar_segundo(lista, nuevo_valor))
        elif opcion == 15:
            print("Lista sin último elemento:", eliminar_ultimo(lista))
        elif opcion == 16:
            valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
            print("Lista sin el valor dado:", eliminar_valor(lista, valor_a_eliminar))
        elif opcion == 17:
            nuevo_elemento = int(input("Ingrese el nuevo elemento a insertar: "))
            posicion = int(input("Ingrese la posición para insertar el nuevo elemento: "))
            print("Lista con nuevo elemento:", insertar_posicion(lista, nuevo_elemento, posicion))
        elif opcion == 18:
            nuevo_elemento = int(input("Ingrese el nuevo elemento a insertar: "))
            print("Lista con elemento al inicio:", insertar_primero(lista, nuevo_elemento))
        elif opcion == 19:
            nuevo_elemento = int(input("Ingrese el nuevo elemento a agregar al final: "))
            print("Lista con elemento agregado al final:", agregar_elemento(lista, nuevo_elemento))
        elif opcion == 20:
            imprimir_lista(lista)
        elif opcion == 21:
            imprimir_inversa(lista)
        elif opcion == 22:
            invertir_lista(lista)
        elif opcion == 23:
            print("Suma de valores:", suma_valores(lista))
        elif opcion == 24:
            ordenar_lista(lista)
        elif opcion == 25:
            duplicar_lista(lista)
        elif opcion == 26:
            a = int(input("Ingrese el índice inicial de la porción: "))
            b = int(input("Ingrese el índice final de la porción: "))
            print("Porción de la lista:", obtener_porcion(lista, a, b))
        else:
            print("Opción no válida. Por favor seleccione un número entre 2 y 26.")

main()
"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Tema: 
=========================================
Fecha: 31 de Octubre de 2024
Autor: Diego Prado Pardo
=========================================
"""

def secuencia_valores(v):
    """ Imprime los valores de la lista en una sola línea, separados por espacios.
    (list) -> None """
    print("Punto 2")
    print(" ".join(map(str, v)))

def linea(lista):
    """ Imprime cada valor de la lista en una línea separada.
    (list) -> None """
    print("Punto 3")
    for v in lista:
        print(v)

def cantidad_elementos(lista):
    """ Devuelve la cantidad de elementos en la lista.
    (list) -> int """
    print("Punto 4")
    return len(lista)

def cantidad_pares(lista):
    """ Devuelve la cantidad de elementos pares en la lista.
    (list) -> int """
    print("Punto 5")
    return sum(1 for v in lista if v % 2 == 0)

def mitad_hasta_final(lista):
    """ Imprime los elementos desde la mitad de la lista hasta el final.
    (list) -> None """
    print("Punto 6")
    for i in range(len(lista) // 2, len(lista)):
        print(lista[i])

def imprimir_pares(lista):
    """ Imprime los elementos en posiciones pares de la lista.
    (list) -> None """
    print("Punto 7")
    for i in range(0, len(lista), 2):
        print(lista[i])

def separar_listas(lista):
    """ Separa la lista en dos mitades.
    (list) -> tuple """
    print("Punto 8")
    mitad = len(lista) // 2
    primera_mitad = lista[:mitad]
    segunda_mitad = lista[mitad:]
    return primera_mitad, segunda_mitad

def concatenar_listas(lista1, lista2):
    """ Concatena dos listas en el orden de lista2 + lista1.
    (list, list) -> list """
    print("Punto 9")
    return lista2 + lista1

def menor_valor(lista):
    """ Devuelve el menor valor en la lista.
    (list) -> int """
    print("Punto 10")
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor

def mayor_valor(lista):
    """ Devuelve el mayor valor en la lista.
    (list) -> int """
    print("Punto 11")
    mayor = lista[0]
    for valor in lista:
        if valor > mayor:
            mayor = valor
    return mayor

def buscar_valor(lista, valor):
    """ Busca un valor en la lista y devuelve su índice, o -1 si no está presente.
    (list, int) -> int """
    print("Punto 12")
    for i, v in enumerate(lista):
        if v == valor:
            return i
    return -1

def posicion_valor(lista, valor):
    """ Devuelve la posición de un valor dado en la lista.
    (list, int) -> int """
    print("Punto 13")
    return buscar_valor(lista, valor)

def modificar_segundo(lista, nuevo_valor):
    """ Modifica el segundo elemento de la lista.
    (list, int) -> list """
    print("Punto 14")
    lista[1] = nuevo_valor
    return lista

def eliminar_ultimo(lista):
    """ Elimina el último elemento de la lista.
    (list) -> list """
    print("Punto 15")
    return lista[:-1]

def eliminar_valor(lista, valor):
    """ Elimina la primera aparición de un valor dado de la lista.
    (list, int) -> list """
    print("Punto 16")
    lista_copia = lista[:]
    lista_copia.remove(valor)
    return lista_copia

def insertar_posicion(lista, valor, posicion):
    """ Inserta un valor en una posición específica de la lista.
    (list, int, int) -> list """
    print("Punto 17")
    lista_copia = lista[:]
    lista_copia.insert(posicion, valor)
    return lista_copia

def insertar_primero(lista, valor):
    """ Inserta un valor en la primera posición de la lista.
    (list, int) -> list """
    print("Punto 18")
    return [valor] + lista

def agregar_elemento(lista, valor):
    """ Agrega un valor al final de la lista.
    (list, int) -> list """
    print("Punto 19")
    lista_copia = lista[:]
    lista_copia.append(valor)
    return lista_copia

def imprimir_lista(lista):
    """ Imprime la lista con corchetes y comas.
    (list) -> None """
    print("Punto 20")
    print(lista)

def imprimir_inversa(lista):
    """ Imprime la lista en orden inverso sin modificarla.
    (list) -> None """
    print("Punto 21")
    print(lista[::-1])

def invertir_lista(lista):
    """ Invierte los elementos de la lista y la imprime junto con la original.
    (list) -> list """
    print("Punto 22")
    lista_inversa = lista[::-1]
    print("Original:", lista)
    print("Inversa:", lista_inversa)
    return lista_inversa

def suma_valores(lista):
    """ Calcula la suma de los valores en la lista.
    (list) -> int """
    print("Punto 23")
    total = 0
    for valor in lista:
        total += valor
    return total

def ordenar_lista(lista):
    """ Ordena la lista e imprime los elementos separados por guiones.
    (list) -> list """
    print("Punto 24")
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
    print("Punto 25")
    lista_copia = [x * 2 for x in lista]
    print("Original:", lista)
    print("Copia:", lista_copia)
    return lista_copia

def obtener_porcion(lista, a, b):
    """ Devuelve una porción de la lista entre las posiciones a y b (inclusive).
    (list, int, int) -> list """
    print("Punto 26")
    return lista[a:b+1]

def main():
    valores = input("Ingrese una lista de valores separados por comas:\n")
    lista = list(map(int, valores.split(",")))  # Convertir cada valor a entero
    print("Punto 1\n", lista)

    # Ejecución de cada función para probar el código
    secuencia_valores(lista)
    linea(lista)
    print("Cantidad de elementos:", cantidad_elementos(lista))
    print("Cantidad de elementos pares:", cantidad_pares(lista))
    mitad_hasta_final(lista)
    imprimir_pares(lista)

    primera_mitad, segunda_mitad = separar_listas(lista)
    print("Primera mitad:", primera_mitad)
    print("Segunda mitad:", segunda_mitad)
    
    lista_concatenada = concatenar_listas(primera_mitad, segunda_mitad)
    print("Concatenación de listas:", lista_concatenada)

    print("Menor valor:", menor_valor(lista))
    print("Mayor valor:", mayor_valor(lista))

    valor_a_buscar = int(input("Ingrese el valor a buscar en la lista: "))
    print("Posición del valor:", posicion_valor(lista, valor_a_buscar))

    nuevo_valor = int(input("Ingrese el nuevo valor para el segundo elemento: "))
    print("Lista modificada:", modificar_segundo(lista, nuevo_valor))

    print("Lista sin último elemento:", eliminar_ultimo(lista))

    valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
    print("Lista sin el valor dado:", eliminar_valor(lista, valor_a_eliminar))

    nuevo_elemento = int(input("Ingrese el nuevo elemento a insertar: "))
    posicion = int(input("Ingrese la posición para insertar el nuevo elemento: "))
    print("Lista con nuevo elemento:", insertar_posicion(lista, nuevo_elemento, posicion))

    print("Lista con elemento al inicio:", insertar_primero(lista, nuevo_elemento))
    print("Lista con elemento al final:", agregar_elemento(lista, nuevo_elemento))

    imprimir_lista(lista)
    imprimir_inversa(lista)

    lista_invertida = invertir_lista(lista)

    print("Suma de valores:", suma_valores(lista))
    ordenar_lista(lista)
    duplicar_lista(lista)

    a = int(input("Ingrese el índice inicial de la porción: "))
    b = int(input("Ingrese el índice final de la porción: "))
    print("Porción de la lista:", obtener_porcion(lista, a, b))

# Llamada a la función main para ejecutar el programa
main()

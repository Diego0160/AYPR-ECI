"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Algoritmo Merge-Sort
===========================================
Fecha: 28 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def dividir_lista(lista):
    """ Divide una lista en dos sublistas de la misma longitud.
    (list) -> list, list """
    mitad = len(lista) // 2
    return lista[:mitad], lista[mitad:]

def imprimir_lados(izq, der):
    """ Imprime los lados izquierdo y derecho en el formato esperado.
    (list, list) -> None """
    print(f"Izquierdo {izq}========    Derecho {der}")

def dividir_recursivamente(lista):
    """ Divide recursivamente la lista en mitades con el formato esperado.
    (list) -> None """
    if len(lista) <= 1:
        return
    
    izq, der = dividir_lista(lista)

    print(f"Izquierdo {izq}")
    if len(izq) > 1:
        dividir_recursivamente(izq)
    elif len(izq) == 1 and len(der) == 1:
        imprimir_lados(izq, der)
    else:
        imprimir_lados(izq, der)

    print(f"Derecho {der}")
    if len(der) > 1:
        dividir_recursivamente(der)
    elif len(izq) > 1:
        imprimir_lados(izq, der)
    else:
        imprimir_lados(izq, der)

def dividir_y_armar_al_reves(lista):
    """ Divide la lista en dos y luego las une en orden inverso.
    (list) -> list """
    izq, der = dividir_lista(lista)
    der_revertido = der[::-1]
    return izq + der_revertido

def mezclar(lista1, lista2):
    """ Mezcla dos listas intercalando sus elementos.
    (list, list) -> list """
    resultado = []
    for i in range(max(len(lista1), len(lista2))):
        if i < len(lista1):
            resultado.append(lista1[i])
        if i < len(lista2):
            resultado.append(lista2[i])
    return resultado


def mezcla_ordenada(lista1, lista2):
    """ Mezcla dos listas ordenadas en una lista ordenada.
    (list, list) -> list """
    resultado = []
    i, j = 0, 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado


def busqueda_binaria(lista, objetivo):
    """ Realiza una búsqueda binaria en una lista ordenada e imprime el recorrido.
    (list, Any) -> int """
    izq, der = 0, len(lista) - 1
    recorrido = []

    while izq <= der:
        medio = (izq + der) // 2
        recorrido.append(lista[medio])

        if lista[medio] == objetivo:
            print(f"Recorrido de búsqueda: {recorrido}")
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1

    print(f"Recorrido de búsqueda: {recorrido}")
    return -1

def main():
    print("Menú:")
    print("1. Dividir en dos  #Se presentan algunos datos adicionales no requeridos")
    print("2. Dividir en dos y armar al revés  #Falto implementarlo mejor")
    print("3. Mezclar")
    print("4. Mezcla ordenada")
    print("5. Búsqueda Binaria  #Falto realizar su recorrido")

    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        lista = input("Ingrese una lista separada por comas: ").split(",")
        dividir_recursivamente(lista)
        print(f"\n{lista}")

    elif opcion == 2:
        lista = input("Ingrese una lista separada por comas: ").split(",")
        lista_revertida = dividir_y_armar_al_reves(lista)
        print(f"Izquierdo {lista[:len(lista)//2]}========    Derecho {lista[len(lista)//2:][::-1]}")

    elif opcion == 3:
        lista1 = input("Ingrese la primera lista separada por comas: ").split(",")
        lista2 = input("Ingrese la segunda lista separada por comas: ").split(",")
        lista_intercalada = mezclar(lista1, lista2)
        print(f"Lista resultante: {lista_intercalada}")

    elif opcion == 4:
        lista1 = input("Ingrese la primera lista ordenada separada por comas: ").split(",")
        lista2 = input("Ingrese la segunda lista ordenada separada por comas: ").split(",")
        lista_mezclada_ordenada = mezcla_ordenada(lista1, lista2)
        print(f"Lista resultante ordenada: {lista_mezclada_ordenada}")

    elif opcion == 5:
        lista = input("Ingrese una lista ordenada separada por comas: ").split(",")
        lista = [int(num) for num in lista]
        objetivo = int(input("Ingrese el elemento a buscar: "))
        indice = busqueda_binaria(lista, objetivo)
        if indice == -1:
            print(f"{objetivo} no se encontró en la lista.")
        else:
            print(f"{objetivo} se encuentra en el índice {indice}.")

main()
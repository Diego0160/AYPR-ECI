"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Taller Archivos tipo texto
===========================================
Fecha: 12 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def leer_archivo(nombre, separador=None):
    """ Lee un archivo de texto línea por línea.
    (str, str) -> list """
    archivo = open(nombre, 'r')
    lineas = []
    archivo.readline()
    
    linea = archivo.readline().strip()
    while linea != '':
        datos = linea.split(separador) if separador else linea.split()
        lineas.append(datos)
        linea = archivo.readline().strip()
    
    archivo.close()
    return lineas

def merge_sort(lista):
    """ Ordena una lista utilizando el algoritmo de merge sort.
    (list) -> list """
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    
    return merge(izq, der)

def merge(izq, der):
    """ Combina dos listas ordenadas en una sola lista ordenada.
    (list, list) -> list """
    resultado = []
    i, j = 0, 0
    
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    while i < len(izq):
        resultado.append(izq[i])
        i += 1
    
    while j < len(der):
        resultado.append(der[j])
        j += 1
    
    return resultado

def busqueda_lineal(lista, b):
    """ Realiza una búsqueda lineal en una lista.
    (list, str) -> int """
    longitud = 0
    while longitud < len(lista):
        if lista[longitud] == b:
            return longitud
        longitud += 1
    return -1

def busqueda_binaria(lista, b):
    """ Realiza una búsqueda binaria recursiva en una lista ordenada.
    (list, str) -> int """
    def busqueda(inicio, fin):
        if inicio > fin:
            return -1
        
        medio = (inicio + fin) // 2
        
        if lista[medio] == b:
            return medio
        elif lista[medio] < b:
            return busqueda(medio + 1, fin)
        else:
            return busqueda(inicio, medio - 1)
    
    return busqueda(0, len(lista) - 1)

def buscar_email(nombre):
    """ Encuentra el correo electrónico de un estudiante dado su nombre.
    (str) -> str """
    datos = leer_archivo('g61.dat')
    nombres = [registro[1].upper() for registro in datos]
    indice = busqueda_lineal(nombres, nombre)
    return datos[indice][0] if indice != -1 else None

def ordenar_nombres():
    """ Ordena los nombres de los estudiantes alfabéticamente.
    () -> list """
    datos = leer_archivo('g61.dat')
    nombres = [registro[1] for registro in datos]
    return merge_sort(nombres)

def ordenar_apellidos_y_nombres_aypr():
    """ Ordena los apellidos y nombres de los estudiantes de AYPR
    () -> list """
    datos = leer_archivo('maraton.csv', ';')
    apellidos_nombres = []

    for registro in datos:
        if len(registro) > 6 and registro[6] == 'AYPR':
            apellidos_nombres.append((registro[0], registro[1], registro[2], registro[3]))

    return merge_sort(apellidos_nombres)

def main():
    print("Menú:")
    print("1. Buscar email")
    print("2. Listar nombres ordenados")
    print("3. Listar apellidos de estudiantes de AYPR")
        
    opcion = input("\nSeleccione una opción: ")
        
    if opcion == '1':
        nombre = input('Nombre completo: ').upper()
        email = buscar_email(nombre)
        if email:
            print(f"Email: {email}")
        else:
            print("No encontrado")
        
    elif opcion == '2':
        nombres = ordenar_nombres()
        for nombre in nombres:
            print(nombre)

    elif opcion == '3':
        apellidos_nombres = ordenar_apellidos_y_nombres_aypr()
        for registro in apellidos_nombres:
            print(" ".join(registro))
        
main()
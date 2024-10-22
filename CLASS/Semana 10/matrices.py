# Definición de una matriz de 2 filas y 3 columnas
matriz = [
    [1, 2, 3],  # Fila 1
    [4, 5, 6]   # Fila 2
]

# Recorremos la matriz e imprimimos cada elemento
# Primer for recorre las filas
for i in range(len(matriz)):
    # Segundo for recorre las columnas dentro de cada fila
    for j in range(len(matriz[0])):
        # Imprimimos el valor en la posición [i][j]
        print(matriz[i][j], end=" ")  # end=" " para mantener los valores de la misma fila juntos
    # Cuando termine de recorrer la fila, imprimimos un salto de línea
    print()

# Ejemplo de cómo añadir más filas o columnas si lo necesitas
matriz.append([7, 8, 9])  # Añadimos una nueva fila a la matriz

# Imprimimos la matriz nuevamente para ver el cambio
print("\nMatriz después de añadir una fila:")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
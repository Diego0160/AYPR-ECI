# Primer corchete accede a la posicion dentro de la fila
# Segundo corchete accede a la posicion dentro de la columna
matriz = [[],[]]
len(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        # Cuando acabe cada fila, hacemos el salto de linea
        print(matriz[i][j], end = " ")

def main():

    datos = input().split()
#    datos = list(map(int, datos))
#    m = int(datos[0])
#    n = int(datos[1])
    datos = [int(x) for x in datos]
    while datos != [0,0]:
        tabla = []
        for i in range(datos[0]):
            linea = input()
            tabla.append(linea)
        print(tabla)
        datos = input().split()
        datos = [int(x) for x in datos]
main()

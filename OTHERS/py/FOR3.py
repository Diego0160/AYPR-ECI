def solicitud():
    opcion= int(input("Digite si desea ver la sumatoria opcion 1 u opcion 2 : "))
    n= int(input("Digite hasta que numero quiere que se repita la sumatoria : "))
    return opcion, n 
def funcion_opcion1(n):
    acum = 0
    for i in range(1,n+1):
        acum += ((2**i) / (3**i)) * ((-1) ** (i+1))
    return acum
def funcion_opcion2(n):
    acum = 0
    cont = 0
    for i in range(0,n):
        acum += (((cont+1)*(cont+2)) / ((3 + (4*i)) ** 2)) * ((-1) ** (i))
        cont += 2
    return acum
def main():
    print("Bienvenidos yo le ayudare a calcular la tendencia de acuerdo a su opcion")
    opcion,n = solicitud()
    if opcion == 1:
        resultado = funcion_opcion1(n)
        print("El resultado es :", resultado)
    elif opcion == 2:
        resultado = funcion_opcion2(n)
        print("El resultado es :",resultado)
    print("Un gusto ayudarlo")

main()

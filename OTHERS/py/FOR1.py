def solicitud():
    n = -1
    while n<=1:
        n = int(input("Digite el numero: "))
    return n

def sumatoria(n):
    sum = 0
    for i in range(1,n+1):
        sum += 3 * i
    return sum

def sumatoriaElevada(n,result):
    elevado = 1
    for i in range(n):
        elevado = elevado * result
    return elevado

def main():
    print("Bienvenidos, yo le ayudare a calcular la funcion")
    n = solicitud()
    suman= sumatoria(n)
    sumaele = sumatoriaElevada(n,suman)
    print("El resultado es : ", sumaele)
    print("Un gusto ayudarle")


main()




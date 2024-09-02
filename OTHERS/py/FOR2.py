def intervalos():
    valorminimo = int(input("Digite el valor minimo : "))
    valormaximo =int(input("Digite el valor maximo : "))
    return valorminimo,valormaximo

def numeroprimo(valor):
    cont = 0
    for i in range(1, valor+1):
        if valor % i == 0:
            cont += 1
    return cont

def mostraroPrimo(valor):
    if numeroprimo(valor) == 2:
        return valor

def main():
    print("Bienvenidos, yo le ayudare a calcular los numeros primos")
    intervalomin,intervalomax = intervalos()
    print("Los numeros primos en ese intervalo son : ")
    for valor in range(intervalomin,intervalomax+1):
      if mostraroPrimo(valor):
            print(valor, end=" ")
    
main()

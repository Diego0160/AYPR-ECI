def solicitar():
    n=int(input("Ingresa hasta que termino"))
    return n 
def opcion1(n):
    acum=0
    for i in range(1,n+1):
        valor=((2**i)*((-1)**(i+1)))/(3**i)
        acum=acum+valor
    print("El resultado es",acum)
def opcion2(n):
    acum=0
    for i in range(1,n+1):
        valor=(1+(2*(i-1)))/((3+(4*(i-1)))**2)
        valor=valor*((-1)**(i+1))
        acum=acum+valor
    print("El resultado es",acum)
def main():
    print(" hola te ayudare a calcular la sumatoria que elijas (opcion1=((2**i)*((-1)**i))/(3**i), ( opcion2= (1+(2*(n-1)))/((3+(4*(n-1)))**2))")
    op=int(input("que opcion deseas?"))
    n=solicitar()
    if op==1: 
        opcion1(n)
    else:
        opcion2(n)
    print("Espero haberte ayudado")
main()
        
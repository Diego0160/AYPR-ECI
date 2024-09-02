def solicitar():
    n=0
    while n<1:
        n=int(input("Ingresa el valor de n"))
        if n<1:
            print("Haz ingresado un valor de n negativo o nulo")
    return n 
def sumatoria(n):
    acum=0
    for i in range(1,n+1):
        valor=3*i 
        acum=acum+valor
    return n,acum
def elevar(n,acum):
    exponen=1
    for i in range(1,n+1):
        exponen=exponen*acum
    print("Tu resultado es",exponen)
def main():
    print("Hola,Te ayudare a calcular la sumatoria (3i)^n desde 1 hasta n")
    n=solicitar()
    n,acum=sumatoria(n)
    elevar(n,acum)
    print("Espero haberte ayudado")
main()
        
    
        
        
    
def solicitar():
    a=int(input("Ingrese el valor menor del intervalo"))
    b=int(input("Ingrese el valor mayor del intervalo"))
    return a,b 
def primo(n):
    cont=0
    for i in range(1,n):
        if n%i==0:
            cont+=1 
    return(n,cont)
def confirmar(n,cont):
    if cont==1:
        print(n,"Es primo")
def main():
    print("Hola,te ayudare a verificar en un intervalo cuales numeros primos hay")
    a,b=solicitar()
    for i in range(a,b+1):
        n,cont=primo(i)
        confirmar(n,cont)
    print("Espero haberte ayudado")
main()
    
    
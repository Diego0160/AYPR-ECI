def es_valido(n):
    if n <= -10000 or n >= 10000:
        return False
    return True

def raindrops(n):
    
    resultado = ""

    if n % 3 == 0:
        resultado += "Pling"
    if n % 5 == 0:
        resultado += "Plong"
    if n % 7 == 0:
        resultado += "Plang"

    if resultado == "":
        resultado = str(n)

    return resultado

def main():
    n = int(input())
    es_valido(n)

    if not es_valido(n):
        print("Número fuera de rango")
    else:
        raindrops(n)
        print(raindrops(n))

main()
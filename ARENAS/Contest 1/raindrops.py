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
    print(raindrops(n))

main()

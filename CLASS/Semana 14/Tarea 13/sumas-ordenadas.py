"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Sumas ordenadas
===========================================
Fecha: 19 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def suma_ordenada(secuencia):
    """ Calcula todas las sumas posibles entre dos elementos de la secuencia y las devuelve ordenadas de manera ascendente.
    (str) -> str """
    numeros = [int(x) for x in secuencia.split(',')]

    sumas = []
    
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            suma = numeros[i] + numeros[j]
            sumas.append(suma)
    
    sumas.sort()
    
    return ','.join(map(str, sumas))

def main():
    entrada = input()
    resultado = suma_ordenada(entrada)
    print(resultado)

main()
"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 5
Programa: Cifrado César
=========================================
Autor: Diego Prado Pardo
=========================================
"""

def desplazar_letra(letra, k):
    """ Desplaza una letra k posiciones si es letra, sino la devuelve igual 
    (str, int) -> str """
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minus = "abcdefghijklmnopqrstuvwxyz"
    
    if letra in mayus:
        pos = mayus.find(letra)
        return mayus[(pos + k) % 26]

    if letra in minus:
        pos = minus.find(letra)
        return minus[(pos + k) % 26]

    return letra

def cifrar(texto, k):
    """ Cifra un texto aplicando desplazamiento k a cada letra 
    (str, int) -> str """
    ans = ""
    for letra in texto:
        ans += desplazar_letra(letra, k)
    return ans

def main():
    N = int(input())
    for i in range(N):
        S = input().strip()
        K = int(input())
        ans = cifrar(S, K)
        print(f"Case{i+1} = {ans}")

main()
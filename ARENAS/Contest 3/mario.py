"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 3
Programa: Jumping Mario
=========================================
Autor: Diego Prado Pardo
=========================================
"""
from sys import stdin

def calc(arr: list[int]):
    h = arr[0]
    high, low = 0,0
    for height in arr[1:]:
        if height > h:
            high += 1
        elif height < h:
            low +=1
        h = height

    return(high,low)
def main():
    for i in range(int(input().strip())):
        input()
        nums = list(map(int, input().strip().split()))
        a, b = calc(nums)
        print( "Case ", i+1,": ", a b)

main()
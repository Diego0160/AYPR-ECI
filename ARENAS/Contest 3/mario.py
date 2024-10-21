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
def calc(arr):
    high, low = 0, 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            high += 1
        elif arr[i] < arr[i-1]:
            low += 1
    return high, low

def main():
    for i in range(int(input().strip())):
        input()
        nums = list(map(int, input().strip().split()))
        a, b = calc(nums)
        print( "Case ", i+1,": ", a b)

main()
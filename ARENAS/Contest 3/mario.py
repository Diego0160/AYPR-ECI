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
def calc(arr: list[int]):
    h = arr[0]
    high, low = 0, 0
    for height in arr[1:]:
        if height > h:
            high += 1
        elif height < h:
            low += 1
        h = height

    return (high, low)

def main():
    t = int(input().strip())

    for i in range(t):
        n = int(input().strip())
        nums = [int(x) for x in input().strip().split()]

        a, b = calc(nums)
        print("Case {}: {} {}".format(i+1, a, b))

main()
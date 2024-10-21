"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 2
Programa: Fibonacci secuencia
=========================================
Autor: Diego Prado Pardo
=========================================
"""
def fibonacci_secuencia(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_secuencia = [0, 1]
        for i in range(2, n + 1):
            fib_secuencia.append(fib_secuencia[-1] + fib_secuencia[-2])
        return fib_secuencia

def main():
    n = int(input())
    print(", ".join(map(str, fibonacci_secuencia(n))))

main()
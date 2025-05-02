"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Un segundo más
=========================================
Fecha: 3 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def segundo_mas(h, m, s):
    """Calcula el tiempo un segundo después de la hora dada.
    (int, int, int) -> int, int, int
    """

    s = s + 1
    if s == 60:
        s = 0
        m = m + 1

    if m == 60:
        m = 0
        h = h + 1

    if h == 24:
        h = 0

    return h, m, s

def main():
    h = int(input('Ingrese el valor de la hora: '))
    m = int(input('Ingrese el valor de los minutos (0-59): '))
    s = int(input('Ingrese el valor de los segundos (0-59): '))

    n_h, n_m, n_s = segundo_mas(h, m, s)

    print(f"{n_h:02}:{n_m:02}:{n_s:02}")

main()
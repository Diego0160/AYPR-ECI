"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Previa 3: Subprogramas y condicionales
=========================================
Fecha: 12 de Septiembre de 2024
Autor: Diego Prado Pardo
=========================================
"""
def subsidio(edad, creencia):
    """Devuelve el valor del subsidio según la edad y creencia,
    (int, str) -> float
    """
    if edad < 18:
        return float('80')
    elif edad > 18 and edad < 50:
        if creencia == 's':
            return float('100')
        elif creencia == 'n':
            return float('20')
    elif edad > 50:
        if creencia == 's':
            return float('120')
        elif creencia == 'n':
            return float('100')

def main():
    edad = int(input('Edad? '))
    creencia = str(input('Sigue siendo niño? (s/n) '))
    r_subsidio = subsidio (edad, creencia)
    print(f'Subsidio ${r_subsidio}')
main()
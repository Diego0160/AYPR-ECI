"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Pangrama
===========================================
Fecha: 3 de Diciembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def es_pangrama(oracion):
    oracion = oracion.lower()
    
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    
    letras_en_oracion = set(oracion)
    
    return alfabeto.issubset(letras_en_oracion)

def main():
    oracion = input()
    
    if es_pangrama(oracion):
        print("Pangrama")
    else:
        print("No es Pangrama")

main()
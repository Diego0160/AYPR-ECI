"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: El Muro
=========================================
Fecha: 21 de Agosto de 2024
Autor: Diego Prado Pardo
=========================================
"""
# Se busca la altura del amigo, la sombra del amigo del escalador y la sombra del muro.
altura_amigo = float(input("Ingresa la altura del amigo del escalador: "))
sombra_amigo = float(input("Ingresa la longitud de la sombra del escalador: "))
sombra_muro = float(input("Ingresa la longitud de la sombra del muro: "))

# Se realiza una relación para hallar la altura del muro.
altura_muro = (altura_amigo * sombra_muro) / sombra_amigo

print(f"La altura del muro es: {round(altura_muro, 2)} metros")
"""
=========================================
AYPR - Algorítmos y programación
Grupo 61
Contest 5
Programa: Boy or Girl
=========================================
Autor: Diego Prado Pardo
=========================================
"""

def nombre_usuario(nombre):
    caracteres = len(set(nombre))
    
    if caracteres % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

def main():
    nombre = input()
    ans = nombre_usuario(nombre)
    print(ans)

main()
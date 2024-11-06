"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Programa: Agenda
===========================================
Fecha: 5 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""

def main():
    num_fechas = int(input())
    agenda = {}

    for _ in range(num_fechas):
        fecha = input()
        num_eventos = int(input())
        
        eventos = []
        for _ in range(num_eventos):
            evento = input()
            eventos.append(evento)
        
        agenda[fecha] = eventos

    for fecha, eventos in agenda.items():
        
        eventos_str = ", ".join(eventos)
        print(f"{fecha}: {eventos_str}")
main()

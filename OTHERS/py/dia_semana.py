#Problema Dias y Numero
#Elaborado por Julian Camilo Lopez

def dia(numero):
        """Funcion que dice el dia de la semana
        segun su numero correspondiente
        (int) -> str
        """
        if numero== 1:
            numero = "Lunes"
            return  numero
        elif numero == 2:
            numero = "Martes"
            return numero
        elif numero == 3:
            numero = "Miercoles"
            return numero
        elif numero == 4:
            numero = "Jueves"
            return numero
        elif numero == 5:
            numero = "Viernes"
            return numero
        elif numero == 6:
            numero = "Sabado"
            return numero
        elif numero == 7:
            numero = "Domingo"
            return numero
        else:
            numero = "Numero de dia no valido"
            return numero
def main():
    eleccion_user = int(input("Ingrese un numero: "))
    nombre_dia = dia(eleccion_user) # Va un numero elejido por el eleccion_user
    print("El dia corresponde a:", nombre_dia)
    
main()
    

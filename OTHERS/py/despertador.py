#Problema Despertador 
#Elaborado por Julian Lopez
def leer_dato(trabajo, vacaciones):
    """funcion que transforma los datos
    (bool,bool) -> bool
    """
    despertador = trabajo and not vacaciones 
    #Se toma un caso cuando toque encender el despertador
    return despertador

def main():
    trabajo_respuesta = input("Tiene trabajo? (si/no): ").lower()  
    if trabajo_respuesta == "no":
        print("No encienda el despertador")
        return
    
    vacaciones_respuesta = input("Está usted de vacaciones? (si/no): ").lower()
    trabajo = trabajo_respuesta == "si"  
    vacaciones = vacaciones_respuesta == "si"
    
    despertador = leer_dato(trabajo, vacaciones)  
    if despertador:
        print("Encienda el despertador")
    else:
        print("No encienda el despertador")

main()


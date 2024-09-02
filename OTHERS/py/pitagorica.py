#Tripleta Pitagorica 
#Elaborado por Julian Lopez 

def  valores (num_1, num_2, num_3):
    """Funcion que retorna valor bool
    a partir de 
    (int,int,int) -> bool
    """
    pit_sum = num_1**2 + num_2**2
    pit_r = num_3**2
    if pit_sum == pit_r:
        return True
    else:
        return False

def main():
    numero_1 = int(input("Seleccione un Numero: "))
    numero_2 = int(input("Seleccione otro Numero: "))
    numero_3 = int(input("Seleccione un Ultimo Numero: "))

    es_tripleta = valores(numero_1,numero_2,numero_3)
    
    if es_tripleta:
        print("Es tripleta Pitagorica")
    else:
        print("No es tripleta Pitagorica ")

main()

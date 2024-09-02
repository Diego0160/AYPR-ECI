# Elaborado por Daniel mosquera
# problema diferencias def pedir_ventas(nombre):
    """Funcion que pide los datos de las listas 
    (str) -> list
    """
    ventas = []
    print("Ingrese las ventas de", nombre, "(separadas por espacios):")
    ventas_input = input().strip().split() 
    for venta in ventas_input:
        ventas.append(int(venta))  
    return ventas

def encontrar_diferencias(ventas_harry, ventas_meghan):
    diferencias = []
    for i in range(len(ventas_harry)):
        if ventas_harry[i] != ventas_meghan[i]:
            diferencias.append(i + 1)  
    return diferencias

def main():
    ventas_harry = pedir_ventas("Harry")
    ventas_meghan = pedir_ventas("Meghan")
    diferencias = encontrar_diferencias(ventas_harry, ventas_meghan)
    if diferencias:
        print(diferencias)
    else:
            print("No hay diferencias.")
main()
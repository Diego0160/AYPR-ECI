def estacion_comidas(pts, origen):
    """Función donde se ganan 100 puntos si se regresa a la estación correcta.
    (int, int) -> int"""
    print()
    sleep(0.5)
    print('Ingresando a la estación comidas ...')
    sleep(1)
    print("Bienvenido, llegaste a comidas, buen apetito")
    pts = pts + 100
    sleep(1)
    try:
        regreso = int(input("Diga el número de la estación a la que regresa: "))
    except:
        print("Entrada inválida, pierdes 20 puntos.")
        pts -= 20
        mensaje1(origen)
        return pts
    
    if regreso == origen:
        print("Regreso correcto.")
    else:
        print("Penalización, la estación dada no coincide con el origen.")
        pts = pts - randint(1, 20)

    mensaje1(origen)  # Siempre regresar a la estación original
    return pts

def estacion_desinfle(pts, origen):
    """Función donde se pierden puntos si no se regresa a la estación correcta.
    (int, int) -> int"""
    print()
    sleep(0.5)
    print('Ingresando a la estación desinfle ...')
    sleep(1)
    print("Lo sentimos, llegó a desinfle.")
    pts -= 30
    try:
        regreso = int(input("Diga número de la estación a la que regresa: "))
    except:
        print("Entrada inválida, pierdes 10 puntos adicionales.")
        pts -= 10
        mensaje1(origen)
        return pts
    
    if regreso == origen:
        print("Regreso correcto.")
    else:
        print("Penalización, la estación dada no coincide con el origen.")
        pts = pts - randint(1, 20)

    mensaje1(origen)  # Siempre regresar a la estación original
    return pts

def es_codigo_repetido(codigo_completo):
    """Encuentra el código de 2 caracteres que se repite 5 veces en una secuencia.
    str -> str o None"""

    # Dividir la cadena en una lista de códigos individuales de 2 caracteres usando list comprehension
    codigos_divididos = [codigo_completo[i:i+2] for i in range(0, len(codigo_completo), 2)]

    # Se crea un diccionario para contar cada digito
    count_codigos = {}
    for codigo in codigos_divididos:
        count_codigos[codigo] = count_codigos.get(codigo, 0) + 1

    # Buscar los códigos que se repiten 5 veces y agregarlos a una lista
    codigos_repetidos = []
    for codigo, count in count_codigos.items():
        if count == 5:
            codigos_repetidos.append(codigo)

    return codigos_repetidos

def main():
    lista_codigos = input('Introduce una lista de 2 caracteres separados por espacio: ')
    codigos_repetidos = es_codigo_repetido(lista_codigos)

    if codigos_repetidos:
    # Se verifica si uno o mas códigos de 2 carácteres se repiten 5 veces
        if len(codigos_repetidos) == 1:
            print("El código que se repite 5 veces es:", codigos_repetidos[0])
        else:
            print("Los códigos que se repiten 5 veces son:")
            for codigo in codigos_repetidos:
                print(codigo)
    else:
        print("No se encontró ningún código que se repita 5 veces.")

main()
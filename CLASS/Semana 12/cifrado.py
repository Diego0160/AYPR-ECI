"""
===========================================
AYPR - Algorítmos y programación
Grupo 61
Problema: El mensaje secreto
===========================================
Fecha: 6 de Noviembre de 2024
Autor: Diego Prado Pardo
===========================================
"""
def cifrar_mensaje(mensaje, desplazamiento):
    """Cifra un mensaje utilizando un desplazamiento en el alfabeto.
    (str, int) -> str"""
    
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    mensaje = mensaje.lower()
    resultado_cifrado = []
    
    desplazamiento = desplazamiento % len(alphabet)

    # Separar el mensaje en palabras para cifrar cada una sin añadir subrayado extra
    for palabra in mensaje.split():
        palabra_cifrada = []
        # Char nos ayuda a identificar si es una letra o un espacio, tambien puede buscar la posición en el alfabeto y aplicar el desplazamiento de cifrado.
        for char in palabra:
            if char in alphabet:
                # Index nos ayuda a ubicar la posición de la letra en el alfabeto.
                indice_original = alphabet.index(char)
                indice_cifrado = (indice_original + desplazamiento) % len(alphabet)
                palabra_cifrada.append(str(indice_cifrado + 1))
        resultado_cifrado.append("_".join(palabra_cifrada))
    
    return " ".join(resultado_cifrado)

def main():
    mensaje = input("Ingrese el mensaje a cifrar: ")
    desplazamiento = int(input("Ingrese el valor de desplazamiento: "))
    
    cifrado = cifrar_mensaje(mensaje, desplazamiento)
    print("\n", cifrado)

main()

l1 = int(input())
l2 = int(input())
l3 = int(input())

if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print("Triangulo Imposible")
else:
    if l1 == l2 == l3:
        perimetro = l1 + l2 + l3
        print("Equilatero, Perimetro es", perimetro)
    
    elif l1 == l2 or l1 == l3 or l2 == l3:
        if l1 == l2:
            producto = l1 * l2
            lado_2 = l3
        elif l1 == l3:
            producto = l1 * l3
            lado_2 = l2
        else:
            producto = l2 * l3
            lado_2 = l1
        diferencia = producto - lado_2
        print("Isosceles, Diferencia es", diferencia)
    
    else:
        if l1 >= l2 and l1 >= l3:
            lado_mas_largo = l1
        elif l2 >= l1 and l2 >= l3:
            lado_mas_largo = l2
        else:
            lado_mas_largo = l3
        print("Escaleno, Lado mas largo es", lado_mas_largo)

def suma(a, b):
    a = int(a)
    b = int(b)
    r = a + b
    return r

def main():
    a = input()
    b = input()

    a_int = int(a)
    b_int = int(b)
    r = suma(a, b)

    if a_int < 0:
        a = '('+str(a_int)+')'
    if b_int < 0:
        b = '('+str(b_int)+')'
    r = str(r)

    print(a,'+',b,'=',r)

main()
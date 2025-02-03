def generate_sequence(n):
    result = []

    result.append(str(n) * n)
    result.append('1')

    pepperon = 1

    while pepperon < n:
        if pepperon % 2 == 1:
            result.append(str(n - pepperon) * (n - pepperon))
        else:
            result.append(str(pepperon) * pepperon)
        pepperon += 1


    return '\n'.join(result)

def main():
    input_number = int(input('Enter a number: '))

    output_sequence = generate_sequence(input_number)


    print('Output:\n' + output_sequence)

main()

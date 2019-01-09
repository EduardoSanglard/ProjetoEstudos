try:

    v1 = int(input('1º valor: '))
    v2 = int(input('2º valor: '))

    if v1 == v2:
        print("Sao iguais")
    elif v1 > v2:
        print("1º valor e maior")
    else:
        print("2º valor e maior")


except ValueError:
    print('Voce nao digitou um numero')
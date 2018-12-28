try:

    int1 = int(input('Primeiro Inteiro: '))
    int2 = int(input('Segundo Inteiro: '))
    real = float(input('Numero Real: '))

    print('Dobro do primeiro com metade do segundo: ', (int1*2)+int2)
    print('Soma do triplo do primeiro com o terceiro: ', (int1*3)+real)
    print('terceiro elevado ao cubo: ', real**3)

except ValueError:
    print('Voce nao digitou um numero')
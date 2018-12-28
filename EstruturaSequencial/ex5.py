try:

    v1 = float(input('Valor em metros: '))

    cent = v1 * 0.01
    print('Centimetros: ', cent)

except ValueError:
    print('Voce nao digitou um numero')
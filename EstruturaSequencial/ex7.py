try:

    lado = float(input('Lado: '))

    valor = (lado ** 2 ) * 2
    print('Dobro da area do quadrado: ', valor)

except ValueError:
    print('Voce nao digitou um numero')
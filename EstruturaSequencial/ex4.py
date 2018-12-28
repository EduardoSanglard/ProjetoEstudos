try:

    b1 = float(input('1º Bimestre: '))
    b2 = float(input('2º Bimestre: '))
    b3 = float(input('3º Bimestre: '))
    b4 = float(input('4º Bimestre: '))

    media = b1+b2+b3+b4 / 4
    print('A media ', media)
except ValueError:
    print('Voce nao digitou um numero')
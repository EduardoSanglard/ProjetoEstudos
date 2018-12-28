from math import ceil

try:

    area = float(input('Area a ser pintada: '))

    litros = ceil(area / 3)
    if litros < 0:
        litros = 1
    latas = ceil(litros / 18)
    if latas < 0:
        latas = 1

    print('Latas a serem compradas', latas)
    print('valor total', latas*80)

except ValueError:
    print('Voce nao digitou um numero')
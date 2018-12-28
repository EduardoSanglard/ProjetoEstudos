import math

try:

    raio = float(input('Raio: '))

    area = math.pi * raio**2
    print('Area: ', area)

except ValueError:
    print('Voce nao digitou um numero')
try:

    altura = float(input('Altura: '))

    ideal = (72.7*altura)-58
    print('Peso ideal: ', ideal)

except ValueError:
    print('Voce nao digitou um numero')
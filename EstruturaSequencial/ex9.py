try:

    far = float(input('Graus Farenheit: '))

    celcius = (5*(far-32)/9)
    print('Celcius: ', celcius)

except ValueError:
    print('Voce nao digitou um numero')
try:

    cel = float(input('Graus Celcius: '))

    far = (cel * 9/5) + 32
    print('Graus Farenheit: ', far)

except ValueError:
    print('Voce nao digitou um numero')
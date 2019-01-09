try:

    v1 = float(input('Valor com sinal: '))

    if v1 >= 0:
        print("Positivo")
    else:
        print("Negativo")

except ValueError:
    print('Voce nao digitou um numero')
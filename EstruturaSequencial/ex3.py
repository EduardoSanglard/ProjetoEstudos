try:

    n1 = float(input('1º Valor: '))
    n2 = float(input('2º Valor: '))

    soma = n1 + n2
    print('A soma: ', soma)
except ValueError:
    print('Voce nao digitou um numero')
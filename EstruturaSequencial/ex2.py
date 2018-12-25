numero = input('Informe o numero: ')

try:
    print('O numero informado foi ', int(numero))
except ValueError:
    print('Voce nao digitou um numero')
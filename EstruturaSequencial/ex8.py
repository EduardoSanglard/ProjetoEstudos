try:

    valorHora = float(input('Quanto voce ganha por hora: '))
    valorMes = float(input('Quantas horas vc trabalha por mes: '))

    valor = valorHora*valorMes
    print('Salario total: ', valor)

except ValueError:
    print('Voce nao digitou um numero')
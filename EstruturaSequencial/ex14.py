try:

    kilos = float(input('Kilos Pescados: '))

    excedente = kilos - 50
    if excedente>0:
        multa = excedente*4
        print('Kilos excedidos: ', excedente)
        print('Multa a ser paga: ', multa)
    else:
        print('Tudo certo!')

except ValueError:
    print('Voce nao digitou um numero')
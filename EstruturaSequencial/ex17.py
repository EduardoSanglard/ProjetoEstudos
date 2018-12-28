from math import ceil

try:

    area = float(input('Area a ser pintada: '))
    tipo = int(input('Metodo de compra:\n0-Apenas latas\n1-Apenas Galoes\n2-Misturar\n'))

    litros = ceil(area / 6)
    litros += litros*0.1
    if litros < 0:
        litros = 1.1

    amount=0
    valor=0

    if tipo==0:
        latas = ceil(litros / 18)
        if latas < 0:
            latas = 1
        amount = str(latas) + ' latas necessarias'
        valor = latas*18
    elif tipo==1:
        galoes = ceil(litros / 3.6)
        if galoes < 0:
            galoes = 1
        amount = str(galoes) + ' galoes necessarios'
        valor = galoes * 25
    elif tipo==2:
        if litros>=18:
            latas = int((litros/18))
            litros -= latas*18
            valor = latas*80
            if litros > 10.8:
                latas += 1
                amount = str(latas) + ' latas necessarias'
                valor += 80
            else:
                galoes = ceil(litros/3.6)
                amount = str(latas)+ ' latas e ' + str(galoes) + ' galoes necessarios'
                valor += galoes*25
        else:
            galoes = ceil(litros / 3.6)
            valor += galoes * 25
            amount = str(galoes) + ' galoes necessarios'
    else:
        print('Opcao invalida')

    print(amount)
    print('Valor total: ', valor)

except ValueError:
    print('Voce nao digitou um numero')
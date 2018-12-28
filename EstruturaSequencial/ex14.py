try:

    altura = float(input('Altura: '))
    sexo = int(input('Escreva o sexo:\n0-Homem\n1-Mulher\n'))

    if sexo==0:
        ideal = (72.7 * altura) - 58
    elif sexo==1:
        ideal = (62.1 * altura) - 44.7
    else:
        ideal = 'Digite 0 ou 1 para o sexo'


    print('Peso ideal: ', ideal)

except ValueError:
    print('Voce nao digitou um numero')
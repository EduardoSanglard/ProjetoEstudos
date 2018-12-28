try:

    valorHora = float(input('Quanto voce ganha por hora: '))
    valorMes = float(input('Quantas horas vc trabalha por mes: '))

    bruto = valorHora * valorMes
    inss = bruto*0.08
    sindicato = bruto*0.05
    ir = bruto*0.11
    print('Salario bruto: ', bruto)
    print('IR (11%): ', ir)
    print('INSS (8%): ', inss)
    print('Sindicato (5%): ', sindicato)
    print('Salario Liquido: ', bruto-(inss+sindicato+ir))



except ValueError:
    print('Voce nao digitou um numero')
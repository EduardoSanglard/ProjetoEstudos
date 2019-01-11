try:

    nota1 = float(input('1 nota: '))
    nota2 = float(input('2 nota: '))

    res = (nota1+nota2)/2

    if res==10:
        print("Aprovado com Distincao")
    elif res>=7:
        print("Aprovado")
    else:
        print("Reprovado")

except ValueError:
    print('Voce nao digitou um numero')
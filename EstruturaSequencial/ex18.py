try:

    arquivo = float(input('Tamanho do arquivo (MB): '))
    link = float(input('Velocidade do link (Mbps): '))

    tempo = (link*arquivo) / 60

    print('Tempo Estimado: ', round(tempo, 2), 'minutos')
except ValueError:
    print('Voce nao digitou um numero')
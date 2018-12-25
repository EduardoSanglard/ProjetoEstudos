import requests
import json


req = None

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com?t='+titulo+'&apikey=12a6af61')
        dicio = json.loads(req.text)
        return dicio
    except:
        print('Erro na conexao')
        return None

def printar(dicio):
    print(dicio['Title'])
    print(dicio['Year'])
    print(dicio['Director'])
    print(dicio['Actors'])
    print(dicio['imdbRating'])


sair = False

while not sair:
    op = input('Escreva o nome de um filme ou SAIR')

    if op =='SAIR':
        sair = True
    else:
        dicio = requisicao(op)
        if dicio['Response'] == 'False':
            print('Filme nao encontrado')
        else:
            printar(dicio)




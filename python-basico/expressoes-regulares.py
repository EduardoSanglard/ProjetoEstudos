import re
import requests

#https://docs.python.org/3/library/re.html
#https://regex101.com/


requisicao = requests.get('http://www.lacoxinha.com.br/contato')

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) #RAW STRING


if padrao:
    print(padrao)
else:
    print('padrao nao encontrado')


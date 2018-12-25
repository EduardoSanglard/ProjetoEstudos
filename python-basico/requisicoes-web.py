import requests #Beautiful Soup 4 BS4 pip install bs4

requisicao = None
texto = None

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://gogle.com'
             }

biscoitos = {'Ultima-visita': '10/11/2018'}

dados = {
    'username': 'guigui',
    'password': 'guigui123'
}

try:
    requisicao = requests.get('http://g1.com.br', headers= cabecalho, cookies=biscoitos, data=dados)
    texto = requisicao.text
except Exception as erro:
    print('Deu ruim: ', erro)


print(texto)

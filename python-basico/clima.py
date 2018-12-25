import requests
import json


cidade = input('Escreva sua cidade: ')

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=3403396f21e5bc36a57a75767a984dc4')


tempo = json.loads(req.text)

print('Condiçao do tempo: ', tempo['weather'][0]['main'])
print('Temperatura', float(tempo['main']['temp']) - 273.15)
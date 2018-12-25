import time

try:
    a = 12/0
    a = '13e122134423'+3
except ZeroDivisionError:
    print("Erro de calculo dividir por 0")
except NameError:
    print("Digitou algo errado!")
except Exception as erro:
    print("Erro de : ", erro)

print("Programa continua normal")

try:
    open("arquivoo.txt")
except Exception as erro:
    print("Aconteceu algum erro: ", erro)

def abre_arquivo():
    try:
        arquivo = open('arquivonaoexiste.txt')
        return True
    except Exception as erro:
        print("Aconteceu algum erro:", erro)
        return False


while not abre_arquivo():
    print('Tentando abrir arquivo')
    time.sleep(6)

print('Consegui abrir o arquivo')

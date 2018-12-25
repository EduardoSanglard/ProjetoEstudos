arquivo = open('arquivo.txt', 'r')
# arquivo = open('arquivo.txt', 'w')
# arquivo = open('arquivo.txt', 'a')
# arquivo = open('arquivo.txt', 'r+')
# arquivo = open('arquivo.txt', 'b')
# arquivo = open('arquivo.txt', 'br')

print(type(arquivo))
print(arquivo)

# for i in range(0, 50):
#     arquivo.write("KKK EAE ARQUIVO CHURROS\n")

print(arquivo.read())

for linha in arquivo:
    print(linha)


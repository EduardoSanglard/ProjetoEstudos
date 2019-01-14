#Abre e salva as informacoes dos usuarios
arquivo = open('usuarios.txt', 'r')

dados = []
total = 0

for linha in arquivo:
    info = linha.split(" ")
    info[1] = round(int(info[1].replace("\n","")) /(1024**2) , 2)
    dados.append(info)
    total += info[1]

for i in range(len(dados)):
    porcentagem = (dados[i][1]/total)*100
    dados[i].append(round(porcentagem, 2))


media = total/len(dados)

arquivo = open('relatorio.txt', 'w')

arquivo.write("ACME Inc.           Uso do espaço em disco pelos usuários\n")
arquivo.write("------------------------------------------------------------------------\n")
arquivo.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")

for i in range(len(dados)):
    arquivo.write(str(i)+ "\t ")
    arquivo.write(str(dados[i][0]))
    utilizado = str(dados[i][1]).split(".")
    espaco = 15 - len(str(dados[i][0])) + (4 - len(utilizado[0]))
    for j in range(espaco):
        arquivo.write(" ")
    arquivo.write(utilizado[0]+","+utilizado[1]+" MB")
    utilizado = str(dados[i][2]).split(".")
    espaco = 14 - len(utilizado[0])
    for j in range(espaco):
        arquivo.write(" ")
    arquivo.write(utilizado[0]+","+utilizado[1]+"%\n")

arquivo.write("\nEspaço total ocupado: "+ str(round(media, 2))+" MB\n")
arquivo.write("Espaço médio ocupado: "+ str(total)+ " MB")
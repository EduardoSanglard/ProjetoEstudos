str1 = input("String 1: ")
str2 = input("String 2: ")
print("Tamanho de "+str1+": "+str(len(str1))+" caracteres")
print("Tamanho de "+str2+": "+str(len(str2))+" caracteres")
if len(str1) == len(str2):
    print("As duas strings sao de tamanhos iguais")
else:
    print("As duas strings sao de tamanhos diferentes")
if str1 == str2:
    print("As duas strings possuem conteudo igual")
else:
    print("As duas strings possuem conteudo diferente")
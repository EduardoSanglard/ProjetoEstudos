data = input("Data de Nascimento: ")
form = data.split("/")
dia = form[0]
mes = form[1]
ano = form[2]
if mes == '01':
    mes = "Janeiro"
elif mes == '02':
    mes = 'Fevereiro'
elif mes == '03':
    mes = 'Março'
elif mes == '04':
    mes = 'Maio'
elif mes == '05':
    mes = 'Abril'
elif mes == '06':
    mes = 'Junho'
elif mes == '07':
    mes = 'Julho'
elif mes == '08':
    mes = 'Agosto'
elif mes == '09':
    mes = 'Setembro'
elif mes == '10':
    mes = 'Outubro'
elif mes == '11':
    mes = 'Novembro'
else:
    mes = 'Dezembrp'
print("Voce nasceu em "+dia+" de "+mes+" de "+ano)
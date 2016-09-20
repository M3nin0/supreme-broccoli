# Calculo de ano Bissexto

ano = int(input("Insira o ano: "))

if (ano % 4) == 0: #and (ano % 100) == 0 and (ano % 400) == 0:
	print ("Este ano é Bissexto")
else:
	print("Este ano não é Bissexto")

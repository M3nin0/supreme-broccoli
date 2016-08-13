valor = int(input("Insira o valor da hora: "))
hora = int(input("Insira a quntidade de horas trabalhadas: "))
sb = valor * hora

if sb <= 900:
	inss = sb * (10 / 100)
	fgts = sb * (11 / 100)
	desc = inss + fgts
	print ("O valor total dos descontos é:",desc,"\nE seu salario liquido é:",sb - desc)

elif sb > 900 and sb <= 1500:
	ir = sb * (5 / 100)
	inss = sb * (10 / 100)
	fgts = sb * (11 / 100)
	desc = inss + fgts + ir
	print ("O valor total dos descontos é:",desc,"\nE seu salario liquido é:",sb - desc)
 
elif sb > 1500 and sb <= 2500:
	ir = sb * (10 / 100)
	inss = sb * (10 / 100)
	fgts = sb * (11 / 100)
	desc = inss + fgts + ir
	print ("O valor total dos descontos é:",desc,"\nE seu salario liquido é:",sb - desc)

elif sb > 2500:
	ir = sb * (20 / 100)
	inss = sb * (10 / 100)
	fgts = sb * (11 / 100)
	desc = inss + fgts + ir
	print ("O valor total dos descontos é:",desc,"\nE seu salario liquido é:",sb - desc)


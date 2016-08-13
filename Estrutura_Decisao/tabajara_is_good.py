s = int(input("Insira o valor de seu salario para saber o reajuste: "))

if s <= 280:
	aumento = s * 20 / 100
	print ("Seu aumento será de R$",aumento,"e seu salario passa a ser R$",s + aumento)

elif s > 280 and s < 700:
	aumento = s * 15 / 100
	print ("Seu aumento será de R$",aumento,"e seu salario passa a ser R$",s + aumento)

elif s >= 700 and s <= 1500:
	aumento = s * 10 / 100
	print ("Seu aumento será de R$",aumento,"e seu salario passa a ser R$", s + aumento)

elif s > 1500:
	aumento = s * 5 / 100
	print ("Seu aumento será de R$",aumento,"e seu salario passa a ser R$",s + aumento)

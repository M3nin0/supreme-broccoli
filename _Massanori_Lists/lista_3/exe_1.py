num = int(input("Insira um numero de 0 a 10: "))

while num > 10 or num < 0:
	num = int(input("Insira o numero novamente\nTem que ser um valor entre 0 e 10\n: "))

print ("O numero esta correto")

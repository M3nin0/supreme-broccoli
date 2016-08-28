# Calculando o valor fatorial

while 1:
	num = int(input("Insira um numero, ou 0 para sair: "))

	c = num
	if num == 0:
		print("Fim =D")
		break
	if num >= 0 and num <= 16:
		for i in range(c - 1):
			c -= 1
			num *= c
			if c <= 0:
				print(num)
	print("O fatorial é",num)
